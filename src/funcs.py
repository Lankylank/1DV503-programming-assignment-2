import CDatabaseManager
import sql
import ui


def CustomSearch(dbm: CDatabaseManager):
  while(True):
    # user input
    chosenPlatform = ui.UserInput("Platform: ")
    # check if the input exists
    if(sql.Exists(dbm, "platform_table", "platform", chosenPlatform) == False):
      print("No results found")
    else:
      break

  while(True):
    # user input
    chosenGenre = ui.UserInput("Genre: ")
    # check if the inpu exists
    if(sql.Exists(dbm, "genre_table", "genre", chosenGenre) == False):
      print("No results found")
    else:

      break
  #user input
  minPrice = ui.UserInputInt("minprice: ")
  maxPrice = ui.UserInputInt("maxprice: ")
  # query the database
  result = sql.CustomSearch(dbm, chosenPlatform, chosenGenre, str(minPrice), str(maxPrice))
  # prints the result
  ui.PrintData(("Games that match your criteria"), result)

  pause = input()


def GamePrintAvailable(dbm: CDatabaseManager):
  # query the database
  games = sql.Select(dbm, "title_table", "title")
  # prints the result
  ui.PrintData(("Available games"), games)
  pause = input()


def GamePrintPrice(dbm: CDatabaseManager):
  # take user inpit
  gameName = ui.UserInput("Enter the game's name: ")
  ui.Clear()
  # query the database
  result = sql.SelectManyThis(dbm, "title_game_store_table", ["game_store", "price"], "title", gameName)
  # prints the result
  ui.PrintData(("Stores and the corrensponding price "), result)
  
  pause = input()


def GamePrintPriceBetween(dbm: CDatabaseManager):
  # user inputs
  minPrice = ui.UserInputInt("Enter minimum price: ")
  maxPrice = ui.UserInputInt("Enter maximum price: ")
  ui.Clear()
  # queries the database
  result = sql.SelectDistinctBetween(dbm, "title_game_store_table", "title", "price", str(minPrice), str(maxPrice))
  # prints the result
  ui.PrintData(("Games within " + str(minPrice) + " and " + str(maxPrice)), result)
  
  pause = input()

###################################################
def GamePrintVerbose(dbm: CDatabaseManager):
  # user input
  gameName = ui.UserInput("\nEnter the name of the game: ")
  ui.Clear()
  # check if the input exists in the datbase
  if(sql.Exists(dbm, "title_table", "title", gameName)):
    # query the database
    result = sql.GameVerbose(dbm, gameName)
    heading = ["Title", "Year", "Publisher", 
              "Genres","Platforms", "Stores", 
              "Min price", "Max price", "Avg price" ]
    # print results
    ui.PrintVertical(heading, result)
  else:
    print("No results for " + gameName)
  pause = input()


#######################################################################################


def PrintAllChoices(dbm: CDatabaseManager, column: str, tableName: str):
  games = sql.SelectDistinctSorted(dbm, column, tableName)
  heading = "All possible " + column +"s to choose from"
  ui.PrintData(heading, games)


def GamesOnYear(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "year", "title_table")
  year = ui.UserInputInt("\nChoose a year: ")
  ui.Clear()
 
  games = sql.SelectThis(dbm, "title_table", "title", "year", str(year))
  ui.PrintData(("All games released year " + str(year)), games)
  
  AskToPrintVerbose(dbm)


def GamesOnPlatform(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "platform", "platform_table")
  platform = ui.UserInput("\nChoose a platform: ")
  ui.Clear()

  games = sql.SelectThis(dbm, "title_platform_table", "title", "platform", platform)
  ui.PrintData(("All games on " + platform), games)
  
  AskToPrintVerbose(dbm)


def GamesOnGenre(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "genre", "genre_table")
  genre = ui.UserInput("\nChoose a genre: ")
  ui.Clear()

  games = sql.SelectThis(dbm, "title_genre_table", "title", "genre", genre)
  ui.PrintData(("All games on " + genre), games)
  
  AskToPrintVerbose(dbm)


def GamesOnStore(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "game_store", "game_store_table")
  store = ui.UserInput("\nChoose a store: ")
  ui.Clear()

  games = sql.SelectThis(dbm, "title_game_store_table", "title", "game_store", store)
  ui.PrintData(("All games on " + store), games)
  
  AskToPrintVerbose(dbm)


def GamesOnPublisher(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "publisher", "title_table")
  publisher = ui.UserInput("\nChoose a publisher: ")
  ui.Clear()

  games = sql.SelectThis(dbm, "title_table", "title", "publisher", publisher)
  ui.PrintData(("All games by " + publisher), games)
  
  AskToPrintVerbose(dbm)


def GamePrintBasic(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")
  ui.Clear()

  result = sql.GameBasic(dbm, gameName)
  heading = ["title", "Year", "Publisher", "Avg price"]
  ui.PrintVertical(heading, result)
  
  pause = input()


def AskToPrintVerbose(dbm: CDatabaseManager):
  while(True):
    userChoice = ui.UserInput(ui.TextColor.PURPLE + 
                  "----------------------------------------\n" + 
                  ui.TextColor.CLEAR + 
                  "Retrieve game specific information? y/N ")
    
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
    break
  