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
  print("2. Show basic info about a game") # show Title, year, publisher, avg price
  print("3. Show all info about a game")
  print("4. Show price and available stores for a given game")
  print("5. Show all games between given price range")
  # function calls are not new lines
  print() # Our most important querys above
  print("6. Show all games from a specific year")  
  print("7. Show all games from a specific publisher") 
  print("8. Show all games from a specific platform") 
  print("9. Show all games from a specific genre") 
  print("10. Show all games from a specific store") 
  print("Q. Quit" + TextColor.CLEAR)
  print(TextColor.BOLD + TextColor.PURPLE + "------------------------------------------------------------------" + TextColor.CLEAR)
  return input()


# not camel case
def PrintOutput_Verbose(heading: list, data: list):
  os.system('cls')  # dont call system specific code if you can avoid it
  for i in range(0, len(heading)):
    tempString = str()
    tempString += heading[i] + ": "
    for j in data:
      tempString += str(j[i])
    print(tempString)


# These print functions should be one
# not camel case
def PrintOutput_BetweenPrices(data: list, min: str, max: str):
  os.system('cls')  # dont call system specific code if you can avoid it
  tempString = ("Games within " + min + " and " + max +
                "\n----------------------------\n")
  for i in data:
    for j in i:
      tempString += j + "\n"
  print(tempString)

# not camel case
def PrintOutput_SingleHeading(heading: str, data: list):
  os.system('cls')  # dont call system specific code if you can avoid it
  print(heading + "\n" + "-" * len(heading))
  for i in data:
    print(i[0])
  

# not camel case
def PrintOutput_DoubleHeading(heading: str, data: list):
  os.system('cls')  # dont call system specific code if you can avoid it
  print(heading + "\n" + "-" * len(heading) + "\n")

  for i in data:
    print(i[0] + ": " + i[1])

# not camel case
def PrintOutput_BasicGameInfo(heading: str, data: list):
  os.system('cls')  # dont call system specific code if you can avoid it
  print(heading + "\n" + "-" * len(heading) + "\n")





  
  

    
