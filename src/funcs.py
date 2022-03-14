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


#####################################################################

# All of these functions do the same thing but exist soley because you copy pasted before
def GenrePrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "genre_table", "genre")
  heading = "All possible genres to choose from"
  ui.PrintOutput_SingleHeading(heading, games)

def PlatformPrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "platform_table", "platform")
  heading = "All possible platforms to choose from"
  ui.PrintOutput_SingleHeading(heading, games)

def StoresPrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "game_store_table", "game_store")
  heading = "All possible stores to choose from"
  ui.PrintOutput_SingleHeading(heading, games)

def YearPrintAll(dbm: CDatabaseManager):
  years = sql.SelectAllDistinctChoices(dbm, "year", "title_table")
  heading = "All possible years to choose from"
  ui.PrintOutput_SingleHeading(heading, years)

def PublisherPrintAll(dbm: CDatabaseManager):
  publishers = sql.SelectAllDistinctChoices(dbm, "publisher", "title_table")
  heading = "All possible publishers to choose from"
  ui.PrintOutput_SingleHeading(heading, publishers)


##########################################################################################

  
def GamesOnYear(dbm: CDatabaseManager):
  #Provide a list of choices
  # If you ask for input to be in a given range you have to validate
  YearPrintAll(dbm)

  year = UserInputInt("\nChoose a year: ")

  games = sql.Select(dbm, "title_table", "title", "year", str(year))
  heading = "All games released year " + str(year)
  ui.PrintOutput_SingleHeading(heading, games)

  # Copy pasted
  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break

def GamesOnPlatform(dbm: CDatabaseManager):
  #Provide a list of choices
  PlatformPrintAll(dbm)

  platform = UserInput("\nChoose a platform: ")

  games = sql.Select(dbm, "title_platform_table", "title", "platform", platform)
  heading = "All games on " + platform
  ui.PrintOutput_SingleHeading(heading, games)

  # Copy pasted
  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break

def GamesOnGenre(dbm: CDatabaseManager):
  #Provide a list of choices
  GenrePrintAll(dbm)

  genre = UserInput("\nChoose a genre: ")

  games = sql.Select(dbm, "title_genre_table", "title", "genre", genre)
  heading = "All games on " + genre
  ui.PrintOutput_SingleHeading(heading, games)

  # Copy pasted
  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break

def GamesOnStore(dbm: CDatabaseManager):
  #Provide a list of choices
  StoresPrintAll(dbm)

  store = UserInput("\nChoose a store: ")

  games = sql.Select(dbm, "title_game_store_table", "title", "game_store", store)
  heading = "All games on " + store
  ui.PrintOutput_SingleHeading(heading, games)

  # Copy pasted
  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break


def GamesOnPublisher(dbm: CDatabaseManager):
  #Provide a list of choices
  PublisherPrintAll(dbm)

  publisher = UserInput("\nChoose a publisher: ")

  games = sql.Select(dbm, "title_table", "title", "publisher", publisher)
  heading = "All games on " + publisher
  ui.PrintOutput_SingleHeading(heading, games)

  while(True):
    print("------------\nY. for game info\nN. return to menu")
    userChoice = UserInput("Choice: ")
    # Terminal binary option should have default answer
    if userChoice.lower() == "y":
      GamePrintVerbose(dbm)
      break
    if(userChoice.lower() == "n"):
      break

def BasicGameInfo(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.BasicGameInfo(dbm, gameName)
  heading = ["title", "Year", "Publisher", "Avg price"]
  ui.PrintOutput_Verbose(heading, result)
