from support import getWordList as gwl

inputFilePath = "texts/test.txt" # input("Path to file :") #file path input

# runtime = 0
# for line in lines:
#     if runtime >= 10 : break
#     print(line)
#     print(line.split())
#     runtime += 1

words =gwl(inputFilePath)
print(words)

outputFilePath = "result/res001.txt"

with open(outputFilePath, "w") as file:
    for i in words:
        file.write(i+'\n')