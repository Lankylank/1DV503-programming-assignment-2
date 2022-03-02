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

DatabaseManager = CDatabaseManager.CDatabaseManager(username, password, host)
DatabaseManager.Connect()
DatabaseManager.SelectDatabase(DB_NAME)
DatabaseManager.ImportData("Game.csv", "game")




#################################################################################################
#################################################################################################
#################################################################################################

tableName = "Game"
schema = "game_title CHAR(64) PRIMARY KEY, year CHAR(64), publisher CHAR(64)"
schema = " (" + schema + ")"
DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )
 

schema = "game_title, year, publisher"
schema = " (" + schema + ")"
values = "'gta', '1908', 'rockstar'"
values = " VALUES(" + values + ")"

DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()



tableName = "realtion"
schema = "game_title CHAR(64), store CHAR(64), FOREIGN KEY (game_title) REFERENCES Game(game_title)"
schema = " (" + schema + ")"
DatabaseManager.cursor.execute("CREATE TABLE " + tableName + schema )
 

schema = "game_title, store"
schema = " (" + schema + ")"
values = "'gta', 'steam'"
values = " VALUES(" + values + ")"
DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()


schema = "game_title, store"
schema = " (" + schema + ")"
values = "'gta', 'ps4'"
values = " VALUES(" + values + ")"
DatabaseManager.cursor.execute("INSERT INTO " + tableName + schema + values)
DatabaseManager.connector.commit()


sql = "SELECT game_title FROM realtion WHERE game_title='gta'"
DatabaseManager.Execute(sql)
result = DatabaseManager.cursor.fetchall()



sql = "UPDATE Game SET year='1367' WHERE game_title='gta'"
DatabaseManager.Execute(sql)
DatabaseManager.connector.commit()




sql = "DELETE store FROM realtion WHERE game_title='gta'"
DatabaseManager.Execute(sql)
DatabaseManager.connector.commit() #*

#################################################################################################
#################################################################################################
#################################################################################################


# Application loop
while(True):
  pass
