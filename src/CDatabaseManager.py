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

    self.connector = mysql.connector.MySQLConnection()  # We have to call the constructor here..
    self.cursor = mysql.connector.cursor.MySQLCursor()  # Same as above

    self.fstream = CFileStream.CFileStream()


  # Use RAII to free our resources
  def __del__(self):
    # Free resources in the reverse order they were allocated.
    self.cursor.close()
    self.connector.close()


  def __GetCursor(self):
    assert self.connector.is_connected()

    try:
      self.cursor = self.connector.cursor()

      # This success msg is  bit verbose..
      # Debugger.successmsg("Retrieved Cursor from established connection")
    except mysql.connector.Error as error:
      Debugger.errormsg(error.msg)
      Debugger.attach()


  # Simply connectes to mysql
  def Connect(self):
    assert self.connector.is_connected() == False

    try:
      self.connector = mysql.connector.connect(user=self.user, 
                                               password=self.password, 
                                               host=self.host)
      
      Debugger.successmsg("Connected to: " + self.host)
      self.__GetCursor()  # We have connected so now get the cursor
    except mysql.connector.Error as error:  # Error codes are returned as exceptions so we handle them here
      Debugger.errormsg(error.msg)
      Debugger.attach() # If we cant access the database the rest of the program is useless so just attach debugger


  # This sets the current "active" database
  def SelectDatabase(self, databaseName: str):
    assert self.connector.is_connected()

    # Since MySQL stores database names in lower case.. we'll force the argument to lower case first
    databaseName = databaseName.lower()
    try:
      self.connector.database = databaseName  # Try selecting the database
      Debugger.successmsg("Selected Database: " + databaseName)
    except mysql.connector.Error as error:
      # If the database does not exist ask if we want to create it
      if(error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR):
        Debugger.warningmsg("Database '" + databaseName + "' does not exist!\n") # Print warning here because it is not necesarily a failure

        choice = input("Would you like to create a database called " + databaseName + "? Y/n ")
        if(choice.lower() == "n"):
          print("Canceling database selection..\n")  # Just print something to confirm the choice
        else: # Yes is default answer so we create the database here
          self.CreateDatabase(databaseName)
          self.connector.database = databaseName
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
    

  def LoadData(self, filename: str):
    assert self.connector.is_connected()
    assert self.connector.database != None

    
    self.fstream.Read(filename)


  def __TableCreate(self, tableName: str, schema: str):
    schema = " (" + schema + ")"
    try:
      self.cursor.execute("CREATE TABLE " + tableName + schema )
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
      self.connector.commit()
    except mysql.connector.Error as error:
      Debugger.errormsg(error.msg)
      Debugger.attach()

  
  def ParseData(self, tableName: str):
    data = self.fstream.Data()
    matrix = list()
    for row in data:
      matrix.append(row)

    schema = str()
    for element in matrix[0]:
      schema += element
      schema += " CHAR(64),"  # Set all datatypes as char* with sizeof 64 bytes, a bit overkill for some.. too bad!
    schema = schema.removesuffix(",") # For the last field we added we must remove the ,

    # Try creating a table with the given schema before inserting data
    if(self.__TableCreate(tableName, schema)):
      schema = schema.replace(" CHAR(64)", "")  # We must remove the datatypes
      for x in range(1, len(matrix)):
        if(matrix[x][0] != "NA"): # Both a planet and a species must have a name
          values = str()
          for y in range(0, len(matrix[x])):
            values += '"' # We want to wrap our value in quotes "value"
            values += matrix[x][y].lower()
            values += '", '
          values = values.removesuffix(", ")  
          self.__TableInsert(tableName, schema, values)


  # Simple wraps load and parse data functions under one function call
  def ImportData(self, filename: str, tableName: str):
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