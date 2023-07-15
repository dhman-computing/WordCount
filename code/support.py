from pathlib import Path
import sqlite3
from tabulate import tabulate


def getWordList(filePath : Path):
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
    The output is a dictinary of dictinaries.
    Corrosponding to each key there is a dictinary of the words where,
    keys are the words and values are the number of their occurences.
    '''
    wordDict = dict()
    for word in words:

        word = word.lower()
        key = word[0:2]

        if wordDict.get(key) is None:
            wordDict[key] = {word : 1}
        
        else:

            if wordDict[key].get(word) is None:
                wordDict[key][word] = 1
            
            else:
                wordDict[key][word] += 1


    return wordDict

def writeToDatabase(dbPath : Path, wordDict : dict[str, dict[str, int]], textName : str):
    '''
    This function takes a dictinary where values are dictinary 
    and add them to a database named in dbPath at a table textName
    '''
    con = sqlite3.connect(dbPath.as_posix())

    crsr = con.cursor()
    
    crsr.execute(f"CREATE TABLE IF NOT EXISTS {textName} (id INT, word TEXT, count INT)")

    sortedKeysWD = sorted(wordDict.keys())
    id = 1
    for index in sortedKeysWD:
        indexDict = wordDict[index]
        sortedKeysID = sorted(indexDict)

        for word in sortedKeysID:
            crsr.execute(f"INSERT INTO {textName} (id, word, count) VALUES (?, ?, ?)", (id, word, indexDict[word]))

    con.commit()
    con.close()
    print("Database Modified.")

    return

def printTableWithDeleteOption(
    dbPath : Path,
    tableName : str,
    delete: bool = False):
    '''
    This function takes a database path and name of a table as input
    and prints out a table after that we can also enable it to delete
    the database.
    '''
    con = sqlite3.connect(dbPath.as_posix())

    crsr = con.cursor()
    crsr.execute(f"SELECT * FROM {tableName}")
    rows = crsr.fetchall()
    columns = [desc[0] for desc in crsr.description]
    print(tabulate(rows, headers=columns, tablefmt="grid"))

    con.close()
    dbPath.unlink()

