import CDatabaseManager
import Debugger
import sql


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

  return sql.CustomSearch(dbm, chosenPlatform, chosenGenre, minPrice, maxPrice)


def GamePrintAll(dbm: CDatabaseManager):
  games = sql.SelectAll(dbm, "title_table")
  
  # Need some formatting
  for game in games:
    print(game[0])  # not ideal


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


def GamePrintPrices(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  result = sql.SelectMany(dbm, "title_game_store_table", ["game_store", "price"], "title", gameName)

  # Need some formatting
  for platform in result:
    print(platform)


# This uses all junction tables so copy pasted from test1
def GamePrintVerbose(dbm: CDatabaseManager):
  gameName = UserInput("Enter the name of the game: ")

  sql = ("SELECT title_table.*, "
        "GROUP_CONCAT(DISTINCT(title_genre_table.genre) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_platform_table.platform) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_game_store_table.game_store) SEPARATOR ', '), "
        "price_statistics.min, price_statistics.max, price_statistics.avg "
        "FROM title_table "
        "JOIN title_genre_table USING (title) "
        "JOIN title_platform_table USING (title) "
        "JOIN title_game_store_table USING (title) "
        "JOIN price_statistics USING (title) "
        "WHERE title_table.title = '" + gameName + "'"
        "GROUP BY title_table.title")

  dbm.Execute(sql)
  result = dbm.Fetchall()

  for res in result:
    print(res)