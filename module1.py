def createfile(file):

    print("press ENTER to end line.\n end - end input file.")
    lines = []
    while True:
        line = input()
        if line=="end":
            break
        else:
            lines.append(line)
    inFile = open(file, "w")
    inFile.write('\n'.join(lines))
    inFile.close()

def output(name):
    file = open(name, "r")
    print(file.read())
    file.close()

def transform(line):
    if len(line) > 0:
        return line[1:len(line)//2] + "!" + line[(len(line)//2):len(line)]

def createnew(oldpath, newpath):
    old = open(oldpath, 'r')
    new = open(newpath, 'w')
    l = old.readlines()
    l1 = list()
    l2 = list()
    for line in l:
        if line[0]=='#':
            line = transform(line)
            l1.append(line)
        else:
            l2.append(line)
    for line in l2:
        if l2[len(l2)-1] == l[len(l)-1]:
            l2[len(l2)-1] += '\n'
        new.write(line)
    for line in l1:
        new.write(line)
    old.close()
    new.close()