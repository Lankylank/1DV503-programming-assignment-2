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




menu = dict()
menu["0"] = funcs.CustomSearch
menu["1"] = funcs.GamePrintAll
menu["2"] = funcs.GamePrintGenre
menu["3"] = funcs.GamePrintPlatform
menu["4"] = funcs.GamePrintPrices
# menu["5"] = funcs.GamePrintVerbose  # requires view table




while(True):
  ui.MainMenu()
  selection = input()
  
  if(selection.lower() == "q"):
    break

  if selection in menu:
    menu[selection](DatabaseManager)
    pause = input()

  
