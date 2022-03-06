import CDatabaseManager
from ast import For
import csv

# Connection details
# set as you wish
username  = "root"
password  = "root"
host      = "127.0.0.1"
DB_NAME   = "game_database"

# Create database object with the  connection details as parameters
DatabaseManager = CDatabaseManager.CDatabaseManager(username, password, host)
DatabaseManager.Connect() # Connect to to database and a crusor with this function
DatabaseManager.SelectDatabase(DB_NAME)
'''
file = open('game_data_ordered.csv')
game_data = csv.reader(file)

matrix = list()
for row in game_data:
  matrix.append(row)

def ForeginKeyCascade(key: str):
  return "FOREIGN KEY(" + key + ") REFERENCES " + key + "_table(" + key + ") ON DELETE CASCADE ON UPDATE CASCADE, "

def ForeginKey(key: str):
  return "FOREIGN KEY(" + key + ") REFERENCES " + key + "_table(" + key + "), "

def PrimaryKey(keys: str):
  return "PRIMARY KEY(" + keys.removesuffix(",") + "),"

def DoublePK(key1: str, key2:str):
  return "PRIMARY KEY(" + key1 + ", " + key2 + "),"

def DoubleAttrib(attrib1: str, attrib2: str, size: str):
  return attrib1 + " VARCHAR(" + size + "), " + attrib2 + " VARCHAR(" + size + "), "
  
#############################################
# primarys
NUM_ATTRIBUTES = 3
NON_CASCADES = 1

def GetAttribs(attributeData: str):
  attributes = list(str())
  attrib = str()
  for char in attributeData:
    if(char == '~'):
      attributes.append(attrib)
      attrib = str() # Reset
    else:
      attrib += char
  attributes.append(attrib)
  return attributes


def CreateScheme(attributes: list):
  scheme = str()
  for i in range(0, len(attributes)):
    # Check the first character of each string in the list
    if(attributes[i][0] == '*'):
      attributes[i] = str(attributes[i]).removeprefix("*")
      scheme += str(attributes[i]).removeprefix("*") + " VARCHAR(64) PRIMARY KEY,"
    else:
      scheme += attributes[i] + " VARCHAR(64),"

  return scheme.removesuffix(",")


def CreateSchemeJunction(attributes: list):
  scheme = str()
  pkeys = str()
  fkeys = str()
  for i in range(0, len(attributes)):
    # Check the first character of each string in the list
    if(attributes[i][0] == '&'):  # FK Cascade symbol
      attributes[i] = str(attributes[i]).removeprefix("&") # Attribute is already a string but intellisense is retarded
      scheme += attributes[i] + " VARCHAR(64),"
      fkeys += ForeginKeyCascade(attributes[i])  
      pkeys += attributes[i] + ","
    elif(attributes[i][0] == '#'):# FK NON Cascade symbol
      attributes[i] = str(attributes[i]).removeprefix("#")
      scheme += attributes[i] + " VARCHAR(64),"
      fkeys += ForeginKey(attributes[i])
      pkeys += attributes[i] + ","
    else:
      scheme += attributes[i] + " VARCHAR(64),"

  scheme += PrimaryKey(pkeys) + fkeys.removesuffix(", ")
  return scheme


def CreateSchemeInsert(attributes: list):
  insertScheme = str()
  for attribute in attributes:
    insertScheme += attribute + ","
  return " (" + insertScheme.removesuffix(",") + ")"


def CreateTableName(attributes: list):
  assert len(attributes) > 0

  return attributes[0] + "_table"

def CreateTableNameJunction(attributes: list):
  assert len(attributes) > 1

  return attributes[0] + "_" + attributes[1] + "_table"
   

print("*****************************************************")
# def LoadData(numJunctions: int):
numTables = len(matrix[0])  # matrix[0] should be an argument
numJunctions = 3
numPrimaryTables = numTables - numJunctions

# For each table in matrix[0]
for i in range(0, numTables):
  attributes = GetAttribs(matrix[0][i])
  if(i < numPrimaryTables):
    scheme = CreateScheme(attributes)
    #print(scheme) # for testing purpose now since no sql intalled
    tableName = CreateTableName(attributes)
  else:
    scheme = CreateSchemeJunction(attributes)
    #print(scheme)
    tableName = CreateTableNameJunction(attributes)

  #Syntax
  # CREATE TABLE table_name (column, column)

  # CreateTable(tableName, scheme)
  DatabaseManager.cursor.execute("CREATE TABLE " + tableName + "(" + scheme + ")")

  insertScheme = CreateSchemeInsert(attributes)

  for j in range(1, len(matrix)):
    values = str()
    attribValues = GetAttribs(matrix[j][i])
    # hack
    if(len(attribValues[0]) < 1):
      break

    ## for single column attributes  NUM_ATTRIBUTES = 0
    NUM_ATTRIBUTES = len(attributes) - 1
    numAdded = 0
    ### SKIPS single column tables
        # in range(1, 1)    skipps the loop for single column tables
####################  SINGLE COLUMN HACK  ##################################
    if len(attributes) == 1:
      values = " VALUES(" + "'" + attribValues[0] + "'," + values ## dont forget '' :)
      values = values.removesuffix(",")
      values += ")"
      # Syntax for INSERT
      # INSERT INTO game (title, year, publisher) VALUES('gta', '2013', 'rockstar')
      print("INSERT INTO " + tableName + insertScheme + values)
      DatabaseManager.cursor.execute("INSERT INTO " + tableName + insertScheme + values)
      DatabaseManager.connector.commit()
      values = str()
############################################################################
    for k in range(1, len(attribValues)):
      values += "'" + attribValues[k] + "'" + ","
      numAdded += 1
     
      if(numAdded == NUM_ATTRIBUTES):
        numAdded = 0
        values = " VALUES(" + "'" + attribValues[0] + "'," + values ## dont forget '' :)
        values = values.removesuffix(",")
        values += ")"
        # Syntax for INSERT
        # INSERT INTO game (title, year, publisher) VALUES('gta', '2013', 'rockstar')
        print("INSERT INTO " + tableName + insertScheme + values)
        DatabaseManager.cursor.execute("INSERT INTO " + tableName + insertScheme + values)
        DatabaseManager.connector.commit()
        values = str()
'''

