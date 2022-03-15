####################################################################
####################### REQUIRES PYHTON 3.9 ########################
# https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes
#####################################################################


# custom modules
import CDatabaseManager
import ui
import funcs

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
menu["1"] = funcs.GamePrintAvailable # OK!
menu["2"] = funcs.GamePrintBasic # OK!
menu["3"] = funcs.GamePrintVerbose # OK!
menu["4"] = funcs.GamePrintPrice # OK!
menu["5"] = funcs.GamePrintPriceBetween # OK!

##### Our most important queries above! ######

menu["6"] = funcs.GamesOnYear # OK!
menu["7"] = funcs.GamesOnPublisher
menu["8"] = funcs.GamesOnPlatform
menu["9"] = funcs.GamesOnGenre
menu["10"] = funcs.GamesOnStore


# Application loop
while(True):
  selection = ui.MainMenu()
  if(selection.lower() == "q"):
    break

  if selection in menu:
    ui.Clear()
    menu[selection](DatabaseManager)
        
