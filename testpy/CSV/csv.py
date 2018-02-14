filePath = "someFile.txt"

fileObject = open(filePath, "r")

for line in fileObject:
    print (line)