# APL

This is a module used to automatically run PyLint on files.

## Examples
There is a [test.py](test.py).
Run this to test:
```
$ python3
...
>>> from APL import apl
>>> apl.getFile("test/test.py")
```
To get the output from many files, run:
```
>>> apl.getAllDir("test")
```
