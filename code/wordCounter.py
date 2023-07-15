# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=trailing-whitespace
# pylint: disable=import-error


from pathlib import Path
from support import getWordList as gwl
from support import addToDict as atd
from support import writeToDatabase as wtd
from support import printTableWithDeleteOption as ptwdo


inputFilePath = Path("texts/alice.txt") # input("Path to file :") #file path input
dbPath = Path("database/database.db") # input("Path to database :") #path to database
textName = inputFilePath.name[0:inputFilePath.name.index('.')]

# runtime = 0
# for line in lines:
#     if runtime >= 10 : break
#     print(line)
#     print(line.split())
#     runtime += 1

words = gwl(inputFilePath)
count = len(words)



# print(words)

wordDict = atd(words)

# outputFilePath = "result/res002.txt"

# with open(outputFilePath, "w") as file:
#     for i in words:
#         file.write(i+'\n')

for key in wordDict:
    print(wordDict[key])

print(f"Total number of words in the test is {count}")

wtd(dbPath, wordDict, textName)

ptwdo(dbPath, textName, delete=True)

print(f"Total number of words in the test is {count}")

# print(wordDict)
