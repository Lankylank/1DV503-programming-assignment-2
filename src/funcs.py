import CDatabaseManager
import Debugger
import sql
import ui
import os


def UserInput(message: str):
  while(True):
    try:
      data = input(message)
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


def UserInputInt(message: str):
  while(True):
    try:
      data = int(input(message))
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


def CustomSearch(dbm: CDatabaseManager):
  while(True):
    chosenPlatform = UserInput("platform: ")
    if(sql.Exists(dbm, "platform_table", "platform", chosenPlatform) == False):
      print("shit doesnt exist bruh")
    else:
      break

  while(True):
    chosenGenre = UserInput("grenre: ")
    if(sql.Exists(dbm, "genre_table", "genre", chosenGenre) == False):
      print("shit doesnt exist bruh")
    else:

      break

  minPrice = UserInputInt("minprice: ")
  maxPrice = UserInputInt("maxprice: ")

  result = sql.CustomSearch(dbm, chosenPlatform, chosenGenre, str(minPrice), str(maxPrice))
  
  headings = "Games that match your criteria"
  ui.PrintOutput_SingleHeading(headings, result)



def GamePrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "title_table", "title")

  heading = "Available games"
  ui.PrintOutput_SingleHeading(heading, games)


def GamePrintGenre(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.Select(dbm, "title_genre_table", "genre", "title", gameName)

  # Need some formatting
  for genre in result:
    print(genre)


def GamePrintPlatform(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.Select(dbm, "title_platform_table", "platform", "title", gameName)

  # Need some formatting
  for platform in result:
    print(platform)


def GamePrintPrice(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.SelectMany(dbm, "title_game_store_table", ["game_store", "price"], "title", gameName)

  heading = "Stores and the corrensponding price "
  ui.PrintOutputDoubleHeading(heading, result)


def GamePrintPriceBetween(dbm: CDatabaseManager):
  minPrice = UserInputInt("Enter minimum price: ")
  maxPrice = UserInputInt("Enter maximum price: ")

  result = sql.SelectDistinctBetween(dbm, "title_game_store_table", "title", "price", str(minPrice), str(maxPrice))

  ui.PrintOutputBetweenPrices(result, str(minPrice), str(maxPrice))


def GamePrintVerbose(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.GameVerbose(dbm, gameName)
  heading = ["Title", "Year", "Publisher", 
             "Platforms", "Genres", "Stores", 
             "Min price", "Max price", "Avg price" ]
  ui.PrintOutput_Verbose(heading, result)


#####################################################################

def PrintAllChoices(dbm: CDatabaseManager, column: str, tableName: str):
  games = sql.SelectAllDistinct(dbm, column, tableName)
  heading = "All possible " + column +"s to choose from"
  ui.PrintOutputSingleHeading(heading, games)

##########################################################################################

def GamesOnYear(dbm: CDatabaseManager):
  # If you ask for input to be in a given range you have to validate
  # Answer: all i ask is for them to choose a year that is an int. i dont care if it
  # is a year that is provided in the terminal, those are just for example search to the user
  #YearPrintAll(dbm)
  PrintAllChoices(dbm, "year", "title_table")
  year = UserInputInt("\nChoose a year: ")
  games = sql.Select(dbm, "title_table", "title", "year", str(year))
  heading = "All games released year " + str(year)
  ui.PrintOutputSingleHeading(heading, games)
  MultiChoice(dbm)

def GamesOnPlatform(dbm: CDatabaseManager):
  #PlatformPrintAll(dbm)
  PrintAllChoices(dbm, "platform", "platform_table")
  platform = UserInput("\nChoose a platform: ")

  games = sql.Select(dbm, "title_platform_table", "title", "platform", platform)
  heading = "All games on " + platform
  ui.PrintOutputSingleHeading(heading, games)
  MultiChoice(dbm)

def GamesOnGenre(dbm: CDatabaseManager):
  #GenrePrintAll(dbm)
  PrintAllChoices(dbm, "genre", "genre_table")
  genre = UserInput("\nChoose a genre: ")

  games = sql.Select(dbm, "title_genre_table", "title", "genre", genre)
  heading = "All games on " + genre
  ui.PrintOutputSingleHeading(heading, games)
  MultiChoice(dbm)

def GamesOnStore(dbm: CDatabaseManager):
  #StoresPrintAll(dbm)
  PrintAllChoices(dbm, "game_store", "game_store_table")
  store = UserInput("\nChoose a store: ")

  games = sql.Select(dbm, "title_game_store_table", "title", "game_store", store)
  heading = "All games on " + store
  ui.PrintOutputSingleHeading(heading, games)
  MultiChoice(dbm)


def GamesOnPublisher(dbm: CDatabaseManager):
  #PublisherPrintAll(dbm)
  PrintAllChoices(dbm, "publisher", "title_table")
  publisher = UserInput("\nChoose a publisher: ")

  games = sql.Select(dbm, "title_table", "title", "publisher", publisher)
  heading = "All games on " + publisher
  ui.PrintOutputSingleHeading(heading, games)
  MultiChoice(dbm)

def BasicGameInfo(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.BasicGameInfo(dbm, gameName)
  heading = ["title", "Year", "Publisher", "Avg price"]
  ui.PrintOutputVerbose(heading, result)


def MultiChoice(dbm: CDatabaseManager):
  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break
    else:
      os.system('cls')
