import mysql.connector
import mysql.connector.cursor
import mysql.connector.errorcode

# Custom
import Debugger
import CFileStream

class CDatabaseManager:
  def __init__(self, user: str, password: str, host: str):
    self.user = user
    self.password = password
    self.host = host
# MySQLConnection is a class that represents an open connection to a database.
# Use 'connector' when creating cursor, 
# because cursor uses this object to know which database to interact with
    self.connector = mysql.connector.MySQLConnection()  # We have to call the constructor here..
    self.cursor = mysql.connector.cursor.MySQLCursor()  # Same as above
# This class uses another class called CFileStream 
# where we choose a file path and reads it and attatches it as an class attribute
    self.fstream = CFileStream.CFileStream()


  # Use RAII to free our resources
  def __del__(self):
    # Free resources in the reverse order they were allocated.
    self.cursor.close()
    self.connector.close()


  def __GetCursor(self): # check if we are connected before we get cursor for our database
    assert self.connector.is_connected()

    try: # use mysqls exceptions to check if it works or not before actually executing it
      self.cursor = self.connector.cursor()

      # This success msg is  bit verbose..
      # Debugger.successmsg("Retrieved Cursor from established connection")
    except mysql.connector.Error as error:
      # here we specify what we want to do if exception is raised
      Debugger.errormsg(error.msg)
      Debugger.attach()


  # Simply connectes to mysql
  def Connect(self):    # Assertion check if we are connected to mysql
    assert self.connector.is_connected() == False

    # We now connect to the database with the given details from main file
    try: 
      self.connector = mysql.connector.connect(user=self.user, 
                                               password=self.password, 
                                               host=self.host)
      
      Debugger.successmsg("Connected to: " + self.host) # Debugger is different functions that takes a str as argument and prints a message depending on how the event went
      self.__GetCursor()  # We have connected so now get the cursor
    except mysql.connector.Error as error:  # Error codes are returned as exceptions so we handle them here
      Debugger.errormsg(error.msg)
      Debugger.attach() # If we cant access the database the rest of the program is useless so just attach debugger

  # Select database if we have one, if not we create one
  # This sets the current "active" database
  def SelectDatabase(self, databaseName: str):
    assert self.connector.is_connected() ## check if we are connected

    # Since MySQL stores database names in lower case.. we'll force the argument to lower case first
    databaseName = databaseName.lower()
    try:
      self.connector.database = databaseName  # Try selecting the database, self.connector is the object that represents an server connection
      Debugger.successmsg("Selected Database: " + databaseName)
    except mysql.connector.Error as error: 
      # If the database does not exist ask if we want to create it

      # error.errno is the error number that we compare with the error code
      # to be able to see if we got that particular error msg
      if(error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR): 
        Debugger.warningmsg("Database '" + databaseName + "' does not exist!\n") # Print warning here because it is not necesarily a failure

        choice = input("Would you like to create a database called " + databaseName + "? Y/n ")
        if(choice.lower() == "n"):
          print("Canceling database selection..\n")  # Just print something to confirm the choice
        else: # Yes is default answer so we create the database here
          self.CreateDatabase(databaseName) # function call to create the database and we pass the given name to it
          self.connector.database = databaseName # connect to the database
      else: # For all other errors we attach debugger
        Debugger.errormsg(error.msg)
        Debugger.attach()
    

  def CreateDatabase(self, name: str):
    assert self.connector.is_connected()

    try:
      self.cursor.execute("CREATE DATABASE " + name.lower())

      Debugger.successmsg("Created Database: " + name.lower())
    except mysql.connector.Error as error:
      Debugger.errormsg(error.msg)
      Debugger.attach()
    

  def LoadData(self, filename: str): ## before loading data, we check the connection to MySQL and we check so that we have a database
    assert self.connector.is_connected() 
    assert self.connector.database != None

    
    self.fstream.Read(filename) # fstream is the object we created at the beginning which contains the data


  def __TableCreate(self, tableName: str, schema: str):
    schema = " (" + schema + ")"
    try:
      self.cursor.execute("CREATE TABLE " + tableName + schema ) # TableName comes from ImportData()
      return True
    except mysql.connector.Error as error:
      if (error.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR):
        Debugger.warningmsg(error.msg + ", canceling table creation..")
        return False
      Debugger.errormsg(error.msg)
      Debugger.attach()
      return False


  # Internal function to insert data into a table
  def __TableInsert(self, tableName: str, schema: str, values: str):
    schema = " (" + schema + ")"
    values = " VALUES(" + values + ")"
    try:
      self.cursor.execute("INSERT INTO " + tableName + schema + values)
      self.connector.commit() # commit the change
    except mysql.connector.Error as error:
      Debugger.errormsg(error.msg)
      Debugger.attach()

  
  def ParseData(self, tableName: str):
    data = self.fstream.Data()  ## here we retrive the data from the file loaded in with the function ImportData()
    matrix = list()
    for row in data: # simply load in each row, this creates a matrix of data(list of list) since the rows already are in a list
      matrix.append(row)

    schema = str() # the schema needs to be a string to be able to pass it to MySQL
    for element in matrix[0]: # since we include the header in the csv file, we use these names to create our table columns
      schema += element  #TODO change CHAR(128) to CHAR(64)
      schema += " CHAR(128),"  # Set all datatypes as char* with sizeof 64 bytes, a bit overkill for some.. too bad!
    schema = schema.removesuffix(",") # For the last field we added we must remove the ,

    # Try creating a table with the given schema before inserting data
    if(self.__TableCreate(tableName, schema)):
      schema = schema.replace(" CHAR(128)", "")  # We must remove the datatypes
      for x in range(1, len(matrix)): # since we now have created the table we dont need CHAR(64) so we remove it to be able to use the column names for inserting data
        if(matrix[x][0] != "NA"): # first column can't be NA # TODO check so it isn't null!
          values = str() # this is where we store all the values for the columns
          for y in range(0, len(matrix[x])): # matrix contains the data
            values += '"' # We want to wrap our value in quotes "value"
            values += matrix[x][y].lower()
            values += '", '
          values = values.removesuffix(", ")  
          self.__TableInsert(tableName, schema, values) # before going to the next row, we have to insert the row we created(values)


  # Simple wraps load and parse data functions under one function call
  def ImportData(self, filename: str, tableName: str): ## We need to pass file name when using this function. this filename is what the other function class uses aswell
    self.LoadData(filename)
    self.ParseData(tableName)


  # Simple wrapper around the execute function
  def Execute(self, sqlString: str):
    try:
      self.cursor.execute(sqlString)
      
    except mysql.connector.Error as error:
      Debugger.errormsg(error.msg)
      Debugger.attach()

    
  # Simple wrapper around the fetchall functiuon
  def Fetchall(self):
    return self.cursor.fetchall()


  # Returns the schema for the given table. As a list were each element is a field
  def GetSchema(self, tableName: str):
    self.cursor.execute("SHOW COLUMNS FROM " + tableName)
    result = self.cursor.fetchall()

    schema = list()
    for element in result:
      schema.append(element[0])

    return schema