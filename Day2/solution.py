import re

inputFile = open("./input.txt", "r")
acc = 0


def verify(lower, upper, val, string):
    print('line: ', lower, upper, val, string)
    c = string.count(val)
    print(c <= int(upper) and c >= int(lower))
    return c <= int(upper) and c >= int(lower)


for aline in inputFile:
    m = re.search("(\d+)-(\d+) (.): (\w+)", aline)
    if verify(m.group(1), m.group(2), m.group(3), m.group(4)):
	acc += 1
    

print(acc)
inputFile.close()




