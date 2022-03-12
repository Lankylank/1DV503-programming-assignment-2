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