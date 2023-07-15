from support import getWordList as gwl
from support import addToDict as atd
from pathlib import Path

inputFilePath = Path("texts/test.txt") # input("Path to file :") #file path input

# runtime = 0
# for line in lines:
#     if runtime >= 10 : break
#     print(line)
#     print(line.split())
#     runtime += 1

words = gwl(inputFilePath)

# print(words)

wordDict = atd(words)

# outputFilePath = "result/res001.txt"

# with open(outputFilePath, "w") as file:
#     for i in words:
#         file.write(i+'\n')

for key in wordDict:
    print(wordDict[key])

# print(wordDict)