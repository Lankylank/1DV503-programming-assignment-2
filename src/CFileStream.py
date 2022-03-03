import os
import csv

#custom
import Debugger
#
class CFileStream:
  def __init__(self):
    self._searchPath = os.getcwd()
    self._csvfile = None


  def __SetSearchPath(self):
    try:
      self._searchPath = input("\nEnter absolute path: ")
      Debugger.successmsg('New directory: "' + self._searchPath + '"')
    except: # Any and all errors? .. needs to be looked at
      Debugger.errormsg("Changing directory failed.")
      Debugger.attach()


  # This is specifcally for csv files now..
  def Read(self, filename: str):
    # To make sure we have the correct CWD..
    print('\nWill look for ' + filename + ' in: "' + self._searchPath + '"')
    choice = input("Is this correct? Y/n ")
    if (choice.lower() == "n"):
      self.__SetSearchPath() # If not, let the user enter absolute path for CWD
  
    try:
      file = open(os.path.join(self._searchPath, filename), "rt")
      
      assert file.readable()
      self._csvfile = csv.reader(file)
      
    except OSError as error:
      Debugger.errormsg(error.strerror)
      Debugger.attach()


  # Just returns the data stored after reading a file
  def Data(self):
    assert self._csvfile != None

    return self._csvfile