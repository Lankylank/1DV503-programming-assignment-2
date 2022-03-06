import csv

file = open('game_data_ordered.csv')
game_data = csv.reader(file)
#total_csv_rows = sum(1 for row in game_data) ## gets the total rows in csv file, 
                                              ## but removes data for some reason
#print(total_csv_rows)

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
    print(scheme) # for testing purpose now since no sql intalled
    tableName = CreateTableName(attributes)
  else:
    scheme = CreateSchemeJunction(attributes)
    print(scheme)
    tableName = CreateTableNameJunction(attributes)

  print(tableName)
  # CreateTable(tableName, scheme)
  ### Add () around scheme when creating table otherwise error
  #__TableInsert() does this automatically anyway ´, only use when testing

  insertScheme = CreateSchemeInsert(attributes)

  for j in range(1, len(matrix)):
    values = str()
    attribValues = GetAttribs(matrix[j][i])
    # hack
    if(len(attribValues[0]) < 1):
      break

    if(len(attribValues) == 1):
      values = " VALUES(" + "'" + attribValues[0] + "')"
      print("INSERT INTO " + tableName + insertScheme + values)
    else:
      NUM_ATTRIBUTES = len(attributes) - 1
      numAdded = 0
      for k in range(1, len(attribValues)):
        values += "'" + attribValues[k] + "'" + ","
        numAdded += 1
        if(numAdded == NUM_ATTRIBUTES):
          numAdded = 0
          values = " VALUES(" + "'" + attribValues[0] + "'," + values
          values = values.removesuffix(",")
          values += ")"
          print("INSERT INTO " + tableName + insertScheme + values)
          values = str()
        





    






""" schemas = list(str())
tmpStr = str()
for i in range(0, NUM_ATTRIBUTES):
  if (i == 0):
    tmpStr += matrix[0][0] + " VARCHAR(64) PRIMARY KEY,"
  else:
    tmpStr += matrix[0][i] + " VARCHAR(64),"
schemas.append(tmpStr.removesuffix(","))

for i in range(NUM_ATTRIBUTES, len(matrix[0])):
  tmpStr = str()
  tmpStr += matrix[0][i] + " VARCHAR(64) PRIMARY KEY"
  schemas.append(tmpStr)
  tmpStr = str()  # Reset string
  tmpStr += DoubleAttrib(matrix[0][0], matrix[0][i], "64")
  tmpStr += DoublePK(matrix[0][0], matrix[0][i])
  tmpStr += ForeginKeyCascade(matrix[0][0])
  if (i < NUM_ATTRIBUTES + NON_CASCADES):
    tmpStr += ForeginKey(matrix[0][i])
  else:
    tmpStr += ForeginKeyCascade(matrix[0][i])
  schemas.append(tmpStr.removesuffix(", "))

print("------------------------------------------")
for schema in schemas:
  print(schema) """

  
#ON DELETE, ON CASCADE <<------ CHECK THIS OUT # https://www.javatpoint.com/mysql-on-delete-cascade #####

'''SYNTAX FOR FOREIGN KEY'''
# column CHAR(64), FOREIGN KEY(column) REFERENCES table(column-1)

'''Syntax for composite key'''
# column-1 CHAR(64), column-2 CHAR(64), PRIMARY KEY (column-1, column-2)

'''Our table syntax should look like this: '''
# title CHAR(64) PRIMARY KEY,year CHAR(64),publisher CHAR(64)
# platform_name CHAR(64) PRIMARY KEY
# title CHAR(64), platform_name CHAR(64), PRIMARY KEY(title, platform_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(platform_name) REFERENCES platform(platform_name)
# genre_name CHAR(64) PRIMARY KEY
# title CHAR(64), genre_name CHAR(64), PRIMARY KEY(title, genre_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(genre_name) REFERENCES genre(genre_name)
# store_name CHAR(64) PRIMARY KEY
# title CHAR(64), store_name CHAR(64), price VARCHAR(10), PRIMARY KEY(title, store_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(store_name) REFERENCES store(store_name)


'''END RESULT SHOULD BE LIKE THIS   (optional table names, if we change remember to change all occurences!!)'''
# CREATE TABLE game_info (title CHAR(64) PRIMARY KEY,year CHAR(64),publisher CHAR(64))

# CREATE TABLE platform (platform_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_platform (title CHAR(64), platform_name CHAR(64), PRIMARY KEY(title, platform_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(platform_name) REFERENCES platform(platform_name))

# CREATE TABLE genre (genre_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_genre (title CHAR(64), genre_name CHAR(64), PRIMARY KEY(title, genre_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(genre_name) REFERENCES genre(genre_name))

# CREATE TABLE store (store_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_store (title CHAR(64), store_name CHAR(64), price VARCHAR(10), PRIMARY KEY(title, store_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(store_name) REFERENCES store(store_name) ON DELETE CASCADE)





# Why not use title TEXT instead of CHAR(64)? 
# TEXT only occupies the actual lenght of the text + 2 bytes
# CHAR size in bytes is number of char
# VARCHAR size in bytes is number of chars used +1
# Isn't it better to dynamically allocate memory instead?
# CHAR allocates a set chunk?

# if we use CHAR, Mysql pads the remainder of spaces that are not used
# VARCHAR are not padded, stores only the lenght of the string + 1 or 2 bytes for a prefix
# TEXT, mysql doesnt support text data types well. Can lead to creation of a temporary table
# on disk instead of memory, which leads to significant performance penalties.
'''https://blog.cpanel.com/varchar-vs-text-for-mysql-databases/'''