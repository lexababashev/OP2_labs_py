from module1 import *

oldpath = "old.txt"
newpath = "new.txt"
createfile(oldpath)
createnew(oldpath, newpath)
print("OLD: ")
output(oldpath)
print("NEW: ")
output(newpath)