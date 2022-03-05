####################################################################
####################### REQUIRES PYHTON 3.9 ########################
# https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes
#####################################################################


# custom modules
import CDatabaseManager

# Connection details
# set as you wish
username  = "root"
password  = "root"
host      = "127.0.0.1"
DB_NAME   = "database_name"


# Create database object with the  connection details as parameters
DatabaseManager = CDatabaseManager.CDatabaseManager(username, password, host)
DatabaseManager.Connect() # Connect to to database and a crusor with this function
DatabaseManager.SelectDatabase(DB_NAME)

# this loads the data and parses it,
#  creates table based on this data and inserts data
####DatabaseManager.ImportData("game_data.csv", "game") 


########   DATAFLOW   ########
# Create databasemanager object
# - create CFileStream object
# Connect() to MySQL
# - Create cursor
# Select Database
# - check if exists, if not:
# - Create Database -> Connect to it
# ImportData()
# - LoadData()
# - check filepath, if not correct -> _setSearchPath()
# - attatch file to CFileStream object
# ParseData()
# - retrive data with: Data(), returns file
# - create list
# - append each csv file row into it
# Create Schema
# - use header as column names
# - attach CHAR(64) for each column
# Create Table with the given schema
# - remove CHAR(64) from schema
# - skip first row (header)
# - load all data of a row into a string called values
# Table insert the values
# REPEAT until all rows in the file has been inserted into the table



##################################################################################################
###########################  EXPERIMENTING  ##################################################
#################################################################################################
### CREATE TABLE
tableName = "game"
schema = "title CHAR(64) PRIMARY KEY, year CHAR(64), publisher CHAR(64)"
schema = " (" + schema + ")"
DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )

### CREATE TABLE
tableName = "genre"
schema = "genre_name CHAR(64) PRIMARY KEY"
schema = " (" + schema + ")"
DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )

### CREATE TABLE
tableName = "game_type"
schema = "title CHAR(64), genre CHAR(64), PRIMARY KEY (title, genre), FOREIGN KEY(title) REFERENCES game(title), FOREIGN KEY(genre) REFERENCES genre(genre_name)"
schema = " (" + schema + ")"
DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )

 

schema = "title, year, publisher"
schema = " (" + schema + ")"
values = "'gta', '2013', 'rockstar'"
values = " VALUES(" + values + ")"

DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()

schema = "title, year, publisher"
schema = " (" + schema + ")"
values = "'Skyrim', '2014', 'bethesda'"
values = " VALUES(" + values + ")"

DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()

schema = "title, year, publisher"
schema = " (" + schema + ")"
values = "'minecraft', '2009', 'Mojan'"
values = " VALUES(" + values + ")"

DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()




#tableName = "realtion"
#schema = "game_title CHAR(64), store CHAR(64), FOREIGN KEY (game_title) REFERENCES Game(game_title)"
#schema = " (" + schema + ")"
#DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )
 

#schema = "game_title, store"
#schema = " (" + schema + ")"
#values = "'gta', 'steam'"
#values = " VALUES(" + values + ")"
#DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
#DatabaseManager.connector.commit()


#schema = "game_title, store"
#schema = " (" + schema + ")"
#values = "'gta', 'ps4'"
#values = " VALUES(" + values + ")"
#DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
#DatabaseManager.connector.commit()


#sql = "SELECT game_title FROM realtion WHERE game_title='gta'"
#DatabaseManager.Execute(sql)
#result = DatabaseManager.cursor.fetchall()



#sql = "UPDATE Game SET year='1367' WHERE game_title='gta'"
#DatabaseManager.Execute(sql)
#DatabaseManager.connector.commit()




#sql = "DELETE store FROM realtion WHERE game_title='gta'"
#DatabaseManager.Execute(sql)
#DatabaseManager.connector.commit() #*

#################################################################################################
#################################################################################################
#################################################################################################


## THIS FOOLED ME, I SAT AND WAITED FOR THE PROGRAM TO END, THOUGHT MY COMPUTER WOULD EXPLODE

## Application loop
#while(True):
#  pass
