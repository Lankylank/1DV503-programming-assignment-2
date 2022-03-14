####################################################################
####################### REQUIRES PYHTON 3.9 ########################
# https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes
#####################################################################


# custom modules
import CDatabaseManager
import ui
import funcs
import os

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
NUM_JUNCTION_TABLES = 3
DatabaseManager.ImportData("game_data_ordered.csv", NUM_JUNCTION_TABLES) 


# Since this is application specific and dbm doesnt support view tables atm i'll put it here
viewTable = (
              "price_statistics AS "
              "SELECT title, min(price) AS min, "
              "max(price) AS max, "
              "round(avg(price)) as avg "
              "FROM title_game_store_table "
              "GROUP BY title"
            )
DatabaseManager.ViewCreate(viewTable)


# The menu is simply a hashmap of function pointers
menu = dict()
menu["0"] = funcs.CustomSearch  # OK!
# Games
menu["1"] = funcs.GamePrintAll # OK!
menu["2"] = print() # get basic info, title, year, publisher, avg price
menu["3"] = funcs.GamePrintVerbose # OK!
menu["4"] = funcs.GamePrintPrice # OK!
menu["5"] = funcs.GamePrintPriceBetween #OK!
menu["6"] = funcs.GamePrintPrice # OK!
menu["7"] = print()
menu["8"] = print()
# Genre
menu["9"] = funcs.GenrePrintAll
# Platform
menu["10"] = funcs.PlatformPrintAll
menu["11"] = funcs.PlatformPrintAll

'''
# formating for out last queries
sql = ("SELECT title_table.*, "
       "title_game_store_table.game_store, "
       "title_game_store_table.price "
       "FROM title_table "
       "JOIN title_genre_table USING (title)"
       "JOIN title_game_store_table USING (title) "
       "WHERE title_genre_table.genre = 'sandbox'")

DatabaseManager.Execute(sql)
result = DatabaseManager.cursor.fetchall()
for i in result:
  print(i)
'''

# application loop
while(True):
  selection = ui.MainMenu()
  if(selection.lower() == "q"):
    break

  if selection in menu:
    os.system('cls') # why isn't Clear() defined?
    menu[selection](DatabaseManager)
    pause = input()

# 0 custom search
# 1 list all game in the database
# 2 get all info of a game
# 3 List all games within a give price range
# 4 list all games from a specific year
# 5 list all games from a specific publisher
# 6 list all games from a specific platform
# 7 list all games from a specific genre
# 8 list all games from a specific store





'''
Option 0.
----------
1. [Option]: --custom search.--
2. ask for users input
    2.1 choose platform
    2.2 choose genre
    2.3 choose price range
3. print result
4. ask for user input
    4.1. [Option]: choose a game from the results
        4.1.1 get all info about game
        4.1.2. get price/store info
        4.1.3. get genre
        4.1.4. get platform
        4.1.5. get publiser/year (published 2019 by "publisher name")
    4.2 [Option]: return to menu 


Option 1.    --list all game in the database.--
---------  

1. [Option]: list all game in the database.
2. print results
3. Ask for user input
  3.1. [Option]: Choose a game from the results
       3.1.1. get all info about the game
       3.1.2. get price/store info
       3.1.3. get genre
       3.1.4. get platform
       3.1.5. get publiser/year (published year 2019 by "publisher name")
  3.2. [Option]: return to menu


Option 2.    --get all info of a game--
---------  

1. [Option]: get all info of a game
2. Ask for user input
    2.1 provide a game name
3. print results
4. [Option]: return to menu


Option 3.   --List all games within a give price range--
---------

1. [Option]: List all games within a give price range
2. Ask for user input
    2.1 lowestPrice
    2.2 highestPrice
3. print result
4. Ask for user input
      4.1. [Option]: Choose a game from the results
          4.1.1. get all info about the game
          4.1.2. get price/store info
          4.1.3. get genre
          4.1.4. get platform
          4.1.5. get publiser/year (published year 2019 by "publisher name")
      4.2. [Option]: return to menu

Option 4.   --list all games from a specific year--
--------

1. [Option]: list all games from a specific year
2. Ask for user input
    2.1 provide a year
3. print results
4. Ask for user input
      4.1. [Option]: Choose a game from the results
          4.1.1. get all info about the game
          4.1.2. get price/store info
          4.1.3. get genre
          4.1.4. get platform
          4.1.5. get publiser/year (published year 2019 by "publisher name")
      4.2. [Option]: return to menu


Option 5.   --list all games from a specific publisher--
--------

1. [Option]: list all games from a specific publisher
2. show all publishers available
3. Ask for user input
    2.1 provide a publisher
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu



Option 6.  --list all games from a specific platform--
--------

1. [Option]: list all games from a specific platform
2. show all platforms available
3. Ask for user input
    2.1 provide a platform
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu



Option 7.  -- list all games from a specific genre--
--------

1. [Option]: list all games from a specific genre
2. show all genre's available
3. Ask for user input
    2.1 provide a genre
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu

Option 8.   --list all games from a specific store--
--------

1. [Option]: list all games from a specific store
2. show all stores available
3. Ask for user input
    2.1 provide a store name
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu


'''