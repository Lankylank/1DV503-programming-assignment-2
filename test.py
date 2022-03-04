import csv

# pythons open method opens the file and returns a file object
file = open('game_data.csv')
game_data = csv.reader(file)
#total_csv_rows = sum(1 for row in game_data)  ## gets the total rows in csv file, bute removes data for some reason
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

  if element == 'year':
    schema_game_info += element
    schema_game_info += " CHAR(64),"
  
  if element == 'platform':
    schema_platform += element
    schema_platform += " CHAR(64) PRIMARY KEY"
    schema_game_platform += element
    schema_game_platform += " CHAR(64)" #TODO ADD FOREGGN KEY (Cant remember syntax atm)

  if element == 'publisher':
    schema_game_info += element
    schema_game_info += " CHAR(64)"
    
  if element == 'genre':
    schema_genre += element
    schema_genre += " CHAR(64) PRIMARY KEY"
    schema_game_genre += element
    schema_game_genre += " CHAR(64)" #TODO FK

  if element == 'game_store':
    schema_game_store += element
    schema_game_store += " CHAR(64) PRIMARY KEY"
    schema_game_price += element
    schema_game_price += " CHAR(64)," #TODO ADD FOREGGN KEY (Cant remember syntax atm)
    schema_game_price += "price CHAR(64)" # this we add at the end of this schema

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





