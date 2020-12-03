import re

inputFile = open("./input.txt", "r")
acc = 0


def verify(lPos, rPos, val, string):
    print('line: ', lPos, rPos, val, string)
    print((string[int(lPos)-1] == val) ^ (string[int(rPos)-1] == val))
    return (string[int(lPos)-1] == val) ^ (string[int(rPos)-1] == val)


for aline in inputFile:
    m = re.search("(\d+)-(\d+) (.): (\w+)", aline)
    if verify(m.group(1), m.group(2), m.group(3), m.group(4)):
	acc += 1
    

print(acc)
inputFile.close()