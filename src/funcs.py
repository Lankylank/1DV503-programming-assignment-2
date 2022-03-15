import CDatabaseManager
import sql
import ui


def CustomSearch(dbm: CDatabaseManager):
  while(True):
    chosenPlatform = ui.UserInput("platform: ")
    if(sql.Exists(dbm, "platform_table", "platform", chosenPlatform) == False):
      print("shit doesnt exist bruh")
    else:
      break

  while(True):
    chosenGenre = ui.UserInput("grenre: ")
    if(sql.Exists(dbm, "genre_table", "genre", chosenGenre) == False):
      print("shit doesnt exist bruh")
    else:

      break

  minPrice = ui.UserInputInt("minprice: ")
  maxPrice = ui.UserInputInt("maxprice: ")

  result = sql.CustomSearch(dbm, chosenPlatform, chosenGenre, str(minPrice), str(maxPrice))
  
  headings = "Games that match your criteria"
  ui.PrintOutputSingleHeading(headings, result)
  pause = input()



def GamePrintAvailable(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "title_table", "title")

  heading = "Available games"
  ui.PrintOutputSingleHeading(heading, games)
  pause = input()


def GamePrintGenre(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")

  result = sql.Select(dbm, "title_genre_table", "genre", "title", gameName)

  # Need some formatting
  for genre in result:
    print(genre)
  pause = input()


def GamePrintPlatform(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")

  result = sql.Select(dbm, "title_platform_table", "platform", "title", gameName)

  # Need some formatting
  for platform in result:
    print(platform)
  pause = input()


def GamePrintPrice(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")

  result = sql.SelectMany(dbm, "title_game_store_table", ["game_store", "price"], "title", gameName)

  heading = "Stores and the corrensponding price "
  ui.PrintOutputDoubleHeading(heading, result)
  pause = input()


def GamePrintPriceBetween(dbm: CDatabaseManager):
  minPrice = ui.UserInputInt("Enter minimum price: ")
  maxPrice = ui.UserInputInt("Enter maximum price: ")

  result = sql.SelectDistinctBetween(dbm, "title_game_store_table", "title", "price", str(minPrice), str(maxPrice))

  ui.PrintOutputBetweenPrices(result, str(minPrice), str(maxPrice))
  pause = input()


def GamePrintVerbose(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")

  result = sql.GameVerbose(dbm, gameName)
  heading = ["Title", "Year", "Publisher", 
             "Platforms", "Genres", "Stores", 
             "Min price", "Max price", "Avg price" ]
  ui.PrintOutputVerbose(heading, result)
  pause = input()


#######################################################################################


def PrintAllChoices(dbm: CDatabaseManager, column: str, tableName: str):
  games = sql.SelectAllDistinct(dbm, column, tableName)
  heading = "All possible " + column +"s to choose from"
  ui.PrintOutputSingleHeading(heading, games)


def GamesOnYear(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "year", "title_table")
  year = ui.UserInputInt("\nChoose a year: ")
  games = sql.Select(dbm, "title_table", "title", "year", str(year))
  heading = "All games released year " + str(year)
  ui.PrintOutputSingleHeading(heading, games)
  AskToPrintVerbose(dbm)


def GamesOnPlatform(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "platform", "platform_table")
  platform = ui.UserInput("\nChoose a platform: ")

  games = sql.Select(dbm, "title_platform_table", "title", "platform", platform)
  heading = "All games on " + platform
  ui.PrintOutputSingleHeading(heading, games)
  AskToPrintVerbose(dbm)


def GamesOnGenre(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "genre", "genre_table")
  genre = ui.UserInput("\nChoose a genre: ")

  games = sql.Select(dbm, "title_genre_table", "title", "genre", genre)
  heading = "All games on " + genre
  ui.PrintOutputSingleHeading(heading, games)
  AskToPrintVerbose(dbm)


def GamesOnStore(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "game_store", "game_store_table")
  store = ui.UserInput("\nChoose a store: ")

  games = sql.Select(dbm, "title_game_store_table", "title", "game_store", store)
  heading = "All games on " + store
  ui.PrintOutputSingleHeading(heading, games)
  AskToPrintVerbose(dbm)


def GamesOnPublisher(dbm: CDatabaseManager):
  PrintAllChoices(dbm, "publisher", "title_table")
  publisher = ui.UserInput("\nChoose a publisher: ")

  games = sql.Select(dbm, "title_table", "title", "publisher", publisher)
  heading = "All games on " + publisher
  ui.PrintOutputSingleHeading(heading, games)
  AskToPrintVerbose(dbm)


def GamePrintBasic(dbm: CDatabaseManager):
  gameName = ui.UserInput("Enter the name of the game: ")

  result = sql.GameBasic(dbm, gameName)
  heading = ["title", "Year", "Publisher", "Avg price"]
  ui.PrintOutputVerbose(heading, result)


def AskToPrintVerbose(dbm: CDatabaseManager):
  while(True):
    userChoice = ui.UserInput("\n\n------------\nRetrieve game specific information? y/N ")
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
    break
  