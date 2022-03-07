import CDatabaseManager
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

GAME_NAME = 'minecraft'

# has to be used when creating a database, otherwise some queries wont work.
# only has to be created once because views auto updates it valuse when the
# normal tables updates. a simple check if exists solves it so it wont cause an error.
def create_priceStatistics_view():
  sql = ("CREATE VIEW price_statistics AS "
        "SELECT title, min(price) AS min, "
        "max(price) AS max, "
        "round(avg(price)) as avg "
        "FROM title_game_store_table "
        "GROUP BY title") ### if we dont have this, it only gets 1 row
  DatabaseManager.Execute(sql)

def getGameInfo(title: str):
  sql = "SELECT * FROM title_table WHERE title = '" + title + "'" 
  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result

def getGameGenres(title: str):
  sql = "SELECT genre FROM title_genre_table WHERE title = '" + title + "'" 
  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result

def getGamePlatforms(title: str):
  sql = "SELECT platform FROM title_platform_table WHERE title = '" + title + "'" 
  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result

def getGamePrices(title: str):
  sql = "SELECT game_store, price FROM title_game_store_table WHERE title = '" + title + "'" 
  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result

### GET ALL THE INFO ABOUT A SPECIFIC GAME ###  MAIN QUERY  ####
def getAll(title: str):
## we has to do this because the table we use, have multiple tuples with the same title
## so we have to use GROUP_CONCAT which groups all of them together into a single row,
## otherwise we would have multiple rows but only with different genre's. Added DISTINCT to this
## because this removes duplicates otherwise we would have the same genre mentioned several times
## because a game has several platforms, it prints all of them out, and if we dont use DISTINCT
## we print the same thing over and over again for each of those specific platforms. We only
## want a single record, of each uniqe information a game has.

## GROUP_CONCAT returns a concatenated string, meaning it groups up all the different entrys
## that a table has and adds them together into a single row. (dev.mysql.com/doc)
  sql = ("SELECT title_table.*, "
        "GROUP_CONCAT(DISTINCT(title_genre_table.genre) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_platform_table.platform) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_game_store_table.game_store) SEPARATOR ', '), "
        "price_statistics.min, price_statistics.max, price_statistics.avg "
        "FROM title_table "
        "JOIN title_genre_table USING (title) "
        "JOIN title_platform_table USING (title) "
        "JOIN title_game_store_table USING (title) "
        "JOIN price_statistics USING (title) "
        "WHERE title_table.title = '" + title + "'"
        "GROUP BY title_table.title")

  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result

# get info about a game within a certain price range
#TODO take user input to determin the price range
def gamesWithinPriceRange(lowestPrice: str, highestPrice: str):
  sql = ("SELECT DISTINCT title "
        "FROM title_game_store_table "
        "WHERE title_game_store_table.price BETWEEN " + lowestPrice + " AND " + highestPrice+"")

  DatabaseManager.Execute(sql)
  result = DatabaseManager.cursor.fetchall()
  return result



# search for a game, get title, min price and what store the price is connected to
# search for a platform and return games and their info(title, year, publisher, avgPrice)
# search for a genre -||-











































## USING GROUP BY HERE only prduces 1 record, it skips all other entrys.
'''
sql = ("SELECT *"
       "FROM title_table "
       "JOIN title_genre_table USING (title) "
       "WHERE title_table.title = 'minecraft'"
       "GROUP BY title_table.title")
DatabaseManager.Execute(sql)
result = DatabaseManager.cursor.fetchall()
for i in result:
  print(i)
'''

### THIS ALSO WORKS #### but no joins, only subqueries
## uses as motivation for our getAll() function.
'''
sql = ("SELECT title_table.*,( "
       "SELECT GROUP_CONCAT(title_genre_table.genre) "
       "FROM title_genre_table "
       "WHERE title_table.title = title_genre_table.title)"
       "FROM title_table "
       "WHERE title_table.title = 'minecraft'")
DatabaseManager.Execute(sql)
result = DatabaseManager.cursor.fetchall()
for i in result:
  print(i)
'''

##########   CREATE DATABSE HERE   ##########################

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