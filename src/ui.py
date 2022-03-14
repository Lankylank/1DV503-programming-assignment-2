# class keyword simply used as a namespace
import os
class TextColor:
    PURPLE = '\033[95m'
    TEAL = '\033[96m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


# hack to clear the screen cross platform
def Clear():
  print("\n" * 50)


def PrintHeadline(string: str):
  Clear()
  print(TextColor.BOLD + TextColor.UNDERLINE + TextColor.PURPLE + string + TextColor.CLEAR)


def PrintData(string: str):
  print(TextColor.TEAL + string + TextColor.CLEAR, end="")


def MainMenu() -> str:
  PrintHeadline("Main Menu")
  print(TextColor.TEAL + "0. Custom Search")
  print("1. Print all available games")
  print("2. Show all info about a game")
  print("3. Print platforms tied to chosen game")
  print("4. Print prices for chosen game")
  print("5. Print litteraly everything for chosen game")
  print("6. Print all available genres")
  print("7. Print all available platforms")
  print("Q. Quit" + TextColor.CLEAR)
  print(TextColor.BOLD + TextColor.PURPLE + "------------------------------------------------------------------" + TextColor.CLEAR)
  return input()


def PrintOutput_Verbose(heading: list, data: list):
  os.system('cls')
  for i in range(0, len(heading)):
    tempString = str()
    tempString += heading[i] + ": "
    for j in data:
      tempString += str(j[i])
    print(tempString)

def PrintOutput_BetweenPrices(data: list, min: str, max: str):
  tempString = ("Games within " + min + " and " + max +
                "\n----------------------------\n")
  for i in data:
    for j in i:
      tempString += j + "\n"
  print(tempString)

def PrintOutput_AllGames(data: list):
  tempString = ("All list of all games" + "\n--------------------\n")
  for i in data:
    for j in i:
      tempString += j + "\n"
  print(tempString)






  
  

    
