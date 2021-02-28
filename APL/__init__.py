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
