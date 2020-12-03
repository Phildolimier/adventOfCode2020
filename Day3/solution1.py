inputFile = open("./input.txt", "r")

xCoord = 0
treeCount = 0

##how can I get the width of first line without calling inputFile.read_line()?
##in this case its fine since coord (0,0) of the first line is always NOT a tree, we can start looking on the second line.

width = len(inputFile.readline())-1

for line in inputFile:
    ##ycoord gets incremented on each line loop iteration
    print(line)
    xCoord = (xCoord + 3) % width
    
    if line[xCoord] == '#':
        print("hit on xCoord ", xCoord)
	treeCount += 1

print(treeCount)