import CDatabaseManager
import Debugger
import sql


def user_input(message: str):
  while(True):
    try:
      data = input(message)
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


def user_input_int(message: str):
  while(True):
    try:
      data = int(input(message))
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


def custom_search(dbm: CDatabaseManager):
  while(True):
    chosenPlatform = user_input("platform: ")
    if(sql.exists(dbm, "platform_table", "platform", chosenPlatform) == False):
      print("shit doesnt exist bruh")
    else:
      break

  while(True):
    chosenGenre = user_input("grenre: ")
    if(sql.exists(dbm, "genre_table", "genre", chosenGenre) == False):
      print("shit doesnt exist bruh")
    else:
      break

  minPrice = user_input_int("minprice: ")
  maxPrice = user_input_int("maxprice: ")

  return sql.custom_search(dbm, chosenPlatform, chosenGenre, minPrice, maxPrice)