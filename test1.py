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
  for attribute in attributes:
    if(attribute[0] == '*'):
      scheme += attribute.removeprefix("*") + " VARCHAR(64) PRIMARY KEY,"
    else:
      scheme += attribute + " VARCHAR(64),"

  return scheme.removesuffix(",")

def CreateJunctionScheme(attributes: list):
  # title CHAR(64), genre_name CHAR(64), 
  # PRIMARY KEY(title, genre_name), 
  # FOREIGN KEY(title) REFERENCES tableName(title), FOREIGN KEY(genre_name) REFERENCES tableName(genre_name)
  scheme = str()
  pkeys = str()
  fkeys = str()
  for attribute in attributes:
    if(attribute[0] == '&'):  # FK Cascade symbol
      attribute = str(attribute).removeprefix("&") # Attribute is already a string but intellisense is retarded
      scheme += attribute + " VARCHAR(64),"
      fkeys += ForeginKeyCascade(attribute)  
      pkeys += attribute + ","
    elif(attribute[0] == '#'):# FK NON Cascade symbol
      attribute = str(attribute).removeprefix("#")
      scheme += attribute + " VARCHAR(64),"
      fkeys += ForeginKey(attribute)
      pkeys += attribute + ","
    else:
      scheme += attribute + " VARCHAR(64),"

  scheme += PrimaryKey(pkeys) + fkeys.removesuffix(", ")
  return scheme



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
    print(scheme) # for testing purpose now since no sql intalled
    # CreateTable(scheme)
  else:
    scheme = CreateJunctionScheme(attributes)
    print(scheme)
    # CreateTable(scheme)
