from module import *
fileAll = "All.txt"
fileSoon = "Soon.txt"
fileLong = "Long.txt"

WantToClear(fileAll, fileSoon, fileLong)
products = NewFile(fileAll)
Diffs = ListOfDiffs(products)

CreatingSoonLong(fileSoon, fileLong, products, Diffs)

print("ALL:")
displayFile(fileAll)
print("SOON:")
displayFile(fileSoon)
print("LONG:")
displayFile(fileLong)

print("==========================================")

deleteExpired(fileSoon, fileLong, products, Diffs)

print("SOON:")
displayFile(fileSoon)
print("LONG:")
displayFile(fileLong)