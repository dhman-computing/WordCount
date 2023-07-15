


def getWordList(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()

    words = []

    for line in lines:
        if line[0] == '#' : continue # # at the begging of the line in a .txt file defines comment
        words += line.split()

    return words
