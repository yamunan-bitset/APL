import os

def install():
  try:
    from pylint import epylint as lint
  except:
    _in = input("Pylint is not installed.\nDo you want to install it? [Y/n] ")
    if _in == "y" or \
      _in == "Y" or \
      _in == "":
      os.system("pip install pylint")
      print("\n\nDone\n\n.")

  print("Pylint is installed")
  os.system("pylint --version")

if __name__ == "__main__":
  install()
