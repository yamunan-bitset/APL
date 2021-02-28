from pylint import epylint as lint
import os


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
  
def getFile(_file: str):
  """
  This is for multiple files.
  It will return the output of the terminal command:
  $ pylint -j <number of files> <files>

  E.g.:
  getAllFile("main.py test.py")
  """
  print(os.popen("pylint -j 1 " + _file).read())

def getAllDir(_dir: str = "."):
  """
  This will find all python files from a 
  specified directory or simple the current 
  working directory.

  E.g.:
  getAllDir()
  """
  for f in os.listdir(_dir):
    if f.endswith(".py"):
      print("Found", f)
      getFile(f"{_dir}/{f}")
