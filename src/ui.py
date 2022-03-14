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
  print("1. Show all available games")
  print("2. Show all info about a game")
  print("3. Search for games between given price range")
  print()
  print("4. Search for games within a given year")
  print("5. Search for games with a given publisher")
  print("6. Search for games witin a given platform")
  print("7. Search for games within a given genre")
  print("8. Search for games within a given store")
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
  os.system('cls')
  tempString = ("Games within " + min + " and " + max +
                "\n----------------------------\n")
  for i in data:
    for j in i:
      tempString += j + "\n"
  print(tempString)

def PrintOutput_SingleHeading(heading: str, data: list):
  os.system('cls')
  tempString = (heading + "\n" + "-" * len(heading))
  for i in data:
    for j in i:
      tempString += j + "\n"
  print(tempString)






  
  

    
