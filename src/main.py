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




menu = {"1" : funcs.PrintAllGames}

while(True):
  ui.MainMenu()
  selection = input()
  menu[selection](DatabaseManager)

  if(selection.lower() == "q"):
    print("quit")
    break
