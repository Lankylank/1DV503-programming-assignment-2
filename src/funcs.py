import CDatabaseManager
import Debugger
import sql
import ui


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
  games = sql.SelectAll(dbm, "title_table")

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
  ui.PrintOutput_DoubleHeading(heading, result)


def GamePrintPriceBetween(dbm: CDatabaseManager):
  minPrice = UserInputInt("Enter minimum price: ")
  maxPrice = UserInputInt("Enter maximum price: ")

  result = sql.SelectDistinctBetween(dbm, "title_game_store_table", "title", "price", str(minPrice), str(maxPrice))

  ui.PrintOutput_BetweenPrices(result, str(minPrice), str(maxPrice))


def GamePrintVerbose(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.GameVerbose(dbm, gameName)
  heading = ["Title", "Year", "Publisher", 
             "Platforms", "Genres", "Stores", 
             "Min price", "Max price", "Avg price" ]
  ui.PrintOutput_Verbose(heading, result)


def GenrePrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "genre_table")
  
  # Need some formatting
  for game in games:
    print(game[0])  # not ideal


def PlatformPrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "platform_table")
  
  # Need some formatting
  for game in games:
    print(game[0])  # not ideal