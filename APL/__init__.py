import os

try:
  from pylint import epylint as lint
except:
  _in = input("pylint is not installed.\nDo you want to install it? [Y/n]")
  if _in == "y" or \
    _in == "Y" or \
    _in == "":
    os.system("pip install pylint")
    print("\n\nDone.")

def getStdout(_file: str) -> str:
  """
  This is used to get the stdout of a file.
  
  E.g.:
  getStdout("main.py")
  """
  return lint.py_run(_file, return_std=True)[0]

def getErr(_file: str) -> str:
  """
  This is to get the error in one file.

  E.g.:
  getErr("main.py")
  """
  return lint.py_run(_file, return_std=True)[1]
  
def getAll(_file: str):
  """
  This is for multiple files.
  It will return the output of the terminal command:
  $ pylint -j <number of files> <files>

  E.g.:
  getAll(["main.py", "test.py"])
  """
  print(os.popen("pylint -j 1 " + _file).read())
