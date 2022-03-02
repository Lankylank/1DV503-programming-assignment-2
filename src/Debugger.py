import pdb

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


def successmsg(msg: str):
  # Sets the text color to fail. Prints the msg. Resets the text color back to default
  print(TextColor.BOLD + TextColor.SUCCESS + msg + TextColor.CLEAR)

def warningmsg(msg: str):
  # Sets the text color to fail. Prints the msg. Resets the text color back to default
  print(TextColor.BOLD + TextColor.WARNING + "\nWARNING!\n" + msg + TextColor.CLEAR)

def errormsg(msg: str):
  # Sets the text color to fail. Prints the msg. Resets the text color back to default
  print(TextColor.BOLD + TextColor.FAIL + "\nERROR!\n" + msg + TextColor.CLEAR)

def attach():
  # Simply attaches the debugger
  pdb.set_trace()