inputFilePath = "texts/test.txt" # input("Path to file :")

with open(inputFilePath, "r") as file:
    lines = file.readlines()

# runtime = 0
# for line in lines:
#     if runtime >= 10 : break
#     print(line)
#     print(line.split())
#     runtime += 1

words = []

for line in lines:
    if line[0] == '#' : continue
    words += line.split()

print(words)

outputFilePath = "result/res001.txt"

with open(outputFilePath, "w") as file:
    for i in words:
        file.write(i+'\n')