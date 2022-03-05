import csv

file = open('game_data_ordered.csv')
game_data = csv.reader(file)
#total_csv_rows = sum(1 for row in game_data) ## gets the total rows in csv file, 
                                              ## but removes data for some reason
#print(total_csv_rows)

matrix = list()
for row in game_data:
  matrix.append(row)

############################################################################
###############     CREATE SCHEMA     HARD CODING FTW!!   ##################
############################################################################

## Main schemas WITH PK
schema_game_info = str()
schema_game_store = str()
schema_genre = str()
schema_platform = str()
# schemas with FK
schema_game_genre = str()
schema_game_platform = str()
schema_game_price = str()

###################################################################
## THIS CREATES ALL OUR SCHEMAS IN ONE FOR LOOP
## EITHER WE CREATE ALL SCHEMAS FIRST AND THEN INSERT ALL DATA
## OR WE CREATE 1 SCHEMA, INSERT DATA, CREATE ANOTHER SCHEMA, INSERT DATA......
## THOUGHTS?
######################################################################

for element in matrix[0]:
  if element == 'title':
    schema_game_info += element
    schema_game_info += " CHAR(64) PRIMARY KEY,"
    schema_game_genre += element
    schema_game_genre += " CHAR(64)," #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    schema_game_platform += element
    schema_game_platform += " CHAR(64)," #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    schema_game_price += element
    schema_game_price += " CHAR(64)," #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    continue ## we don't need to continue the loop

  if element == 'year':
    schema_game_info += element
    schema_game_info += " CHAR(64),"
    continue ## we don't need to continue the loop
  
  if element == 'platform':
    schema_platform += element
    schema_platform += " CHAR(64) PRIMARY KEY"
    schema_game_platform += element
    schema_game_platform += " CHAR(64)" #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    continue ## we don't need to continue the loop

  if element == 'publisher':
    schema_game_info += element
    schema_game_info += " CHAR(64)"
    continue ## we don't need to continue the loop

  if element == 'genre':
    schema_genre += element
    schema_genre += " CHAR(64) PRIMARY KEY"
    schema_game_genre += element
    schema_game_genre += " CHAR(64)" #TODO 
    continue ## we don't need to continue the loop

  if element == 'game_store':
    schema_game_store += element
    schema_game_store += " CHAR(64) PRIMARY KEY"
    schema_game_price += element
    schema_game_price += " CHAR(64)," #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    schema_game_price += "price CHAR(64)" # this we add at the end of this schema



# PRINT TO SHOW HOW THE SCHEMAS LOOK
print()
print("MAIN SCHEMAS WITH PRIMARY KEY") ## WE NEED TO CREATE THESE TABLES FIRST (Because of FK)
print(schema_game_info)  # title, year, publisher
print(schema_game_store) # game_store
print(schema_genre) # genre
print(schema_platform) # platform
print("-------")
print("SCHEMAS WITH FOREIGN KEYS ONLY")
print(schema_game_genre) # title, genre
print(schema_game_platform) # title, platform
print(schema_game_price) # title, game_store, price


# COULD DO THIS ASWELL
schema_game_info = matrix[0][0] + " CHAR(64) PRIMARY KEY," + matrix[0][1] + " CHAR(64)," + matrix[0][3] + " CHAR(64)"
print("------\nTEST SCHEMA\n" + schema_game_info)

# this works just aswell
schema_game_info = "title CHAR(64) PRIMARY KEY, year CHAR(64), publisher CHAR(64)"


#############################################
# primarys
NUM_ATTRIBUTES = 3
schemas = list(str())
tmpStr = str()
for i in range(0, NUM_ATTRIBUTES):
  if (i == 0):
    tmpStr += matrix[0][0] + " CHAR(64) PRIMARY KEY,"
  else:
    tmpStr += matrix[0][i] + " CHAR(64),"
schemas.append(tmpStr.removesuffix(","))

for i in range(NUM_ATTRIBUTES, len(matrix[0])):
  tmpStr = str()
  tmpStr += matrix[0][i] + " CHAR(64) PRIMARY KEY"
  schemas.append(tmpStr)
  tmpStr = str()  # Reset string
  tmpStr += matrix[0][0] + " CHAR(64) FOREGIN KEY,"
  tmpStr += matrix[0][i] + " CHAR(64) FOREGIN KEY"
  schemas.append(tmpStr)

print("------------------------------------------")
for schema in schemas:
  print(schema)

  
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
# title CHAR(64), store_name CHAR(64), price CHAR(64), PRIMARY KEY(title, store_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(store_name) REFERENCES store(store_name)


'''END RESULT SHOULD BE LIKE THIS   (optional table names, if we change remember to change all occurences!!)'''
# CREATE TABLE game_info (title CHAR(64) PRIMARY KEY,year CHAR(64),publisher CHAR(64))

# CREATE TABLE platform (platform_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_platform (title CHAR(64), platform_name CHAR(64), PRIMARY KEY(title, platform_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(platform_name) REFERENCES platform(platform_name))

# CREATE TABLE genre (genre_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_genre (title CHAR(64), genre_name CHAR(64), PRIMARY KEY(title, genre_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(genre_name) REFERENCES genre(genre_name))

# CREATE TABLE store (store_name CHAR(64) PRIMARY KEY)
# CREATE TABLE game_store (title CHAR(64), store_name CHAR(64), price CHAR(64), PRIMARY KEY(title, store_name), FOREIGN KEY(title) REFERENCES game_info(title), FOREIGN KEY(store_name) REFERENCES store(store_name))
