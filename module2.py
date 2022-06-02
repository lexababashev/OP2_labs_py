import pickle
from datetime import *

def NewFile(fileName):
    with open(fileName, 'ab') as file:
        products = []
        while True:
            product = {
                "name":str(input("name of product: ")),
                "start":str(input("date of release: ")),
                "end":str(input("date of expiration: "))
            }
            products.append(product)
            res = str(input("Continue? yes or no: "))
            while res != 'yes' and res != 'no':
                res = str(input("Press yes or no: "))
            if res == "no":
                break
        pickle.dump(products,file)
        return products

def WantToClear(file1, file2, file3):
    res = input("click 1 to overwrite file or 2 to append it: ")
    while res != '1' and res != '2':
        res = str(input("click 1 to overwrite file or 2 to append it: "))
    if res == "1":
        clearFile(file1)
        clearFile(file2)
        clearFile(file3)

def isOutOfDate(product):
    DateOfToday = date.today()
    startdate = DateOfToday.strftime("%d.%m.%Y")
    lastdate = product["end"]
    start = datetime.strptime(startdate, "%d.%m.%Y")
    end = datetime.strptime(lastdate, "%d.%m.%Y")
    day = end - start
    Days = day.days
    if Days < 0:
        return True
    else:
        return False

def daysDiff(product):
    firstdate = product["start"]
    lastdate = product["end"]
    t1 = datetime.strptime(firstdate, "%d.%m.%Y")
    t2 = datetime.strptime(lastdate, "%d.%m.%Y")
    day = t2-t1
    return day.days

def ListOfDiffs(products):
    diffs = []
    for product in products:
        day = daysDiff(product)
        diffs.append(day)
    return diffs

def CreatingSoonLong(fileSoon, fileLong, products, diffs):
    file1 = open(fileSoon, 'ab')
    file2 = open(fileLong, 'ab')
    soonProd = []
    longProd = []
    for i in range(0, len(diffs)):
        if diffs[i] <=5:
            soonProd.append(products[i])
        else:
            longProd.append(products[i])
    pickle.dump(soonProd, file1)
    pickle.dump(longProd, file2)
    file1.close()
    file2.close()


def deleteExpired(fileSoon, fileLong, products, diffs):
    file1 = open(fileSoon, 'wb')
    file2 = open(fileLong, 'wb')
    soonProd = []
    longProd = []
    for i in range(0, len(diffs)):
        if isOutOfDate(products[i]):
            continue
        else:
            if diffs[i] <=5:
                soonProd.append(products[i])
            else:
                longProd.append(products[i])

    pickle.dump(soonProd, file1)
    pickle.dump(longProd, file2)
    file2.close()
    file1.close()

def clearFile(file):
    with open(file,'wb') as clear_file:
        pass

def readPickle(fileName):
    with open(fileName, 'rb') as file:
        while True:
            try:
                yield pickle.load(file)
            except EOFError:
                break

def displayFile(fileName):
    for items in readPickle(fileName):
        for item in items:
            print(item["name"])