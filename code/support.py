from pathlib import Path


def getWordList(filePath):
    '''Get a list of words from a .txt file. 
    Here fileName is an instance of Path object in pathlib to the file, 
    from which the word list is to extracted.
    fileName obeys same constraints as path in open function'''

    with filePath.open(mode = "r") as file:
        lines = file.readlines()

    words = []

    for line in lines:
        print(line.rstrip("\n"))
        if line[0] == '#' : continue # '#' at the begging of the line in a .txt file defines comment
        words += line.rstrip("\n").split()

    return words


# def addToDict(words: list):
#     wordDict = dict()
#     for word in words: