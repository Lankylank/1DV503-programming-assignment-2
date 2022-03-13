# class keyword simply used as a namespace
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


def MainMenu():
  PrintHeadline("Main Menu")
  print(TextColor.TEAL + "1. Print all available games")
  print("2. Print genres tied to chosen game")
  print("3. Print platforms tied to chosen game")
  print("4. Print prices for chosen game")
  print("Q. Quit" + TextColor.CLEAR)
  print(TextColor.BOLD + TextColor.PURPLE + "------------------------------------------------------------------" + TextColor.CLEAR)


