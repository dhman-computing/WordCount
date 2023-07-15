from pathlib import Path


def getWordList(filePath):
    '''
    Get a list of words from a .txt file. 
    Here fileName is an instance of Path object in pathlib to the file, 
    from which the word list is to extracted.
    '''

    with filePath.open(mode = "r") as file:
        lines = file.readlines()

    words = []

    for line in lines:
        # print(line.rstrip("\n"))
        if line[0] == '#' : continue # '#' at the begging of the line in a .txt file defines comment
        words += line.rstrip("\n").split()

    return words


def addToDict(words: list[str]):
    '''
    This function gets a list of word and add them to a dictionary,
    where the keys of the dictinary are the first two letters of the word.
    Before adding to the dictinary the words are smallerd.
    '''
    wordDict = dict()
    for word in words:

        key = word[0:2]

        if wordDict.get(key) is None:
            wordDict[key] = [word.lower()]
        
        elif wordDict.get(key) is not None:
            wordDict[key].append(word.lower())

    return wordDict

