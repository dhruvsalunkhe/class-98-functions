from os import read, renames


def countwordsfromthefile():
    filename = input("enter the name of the file")
    f=open(filename,"r")
    # lines = f.read()
    # print(lines)

    numberofwords = 0

    for line in f:
        words=line.split()
        print(words)

        numberofwords = numberofwords + len(words)


    print(numberofwords)
countwordsfromthefile()