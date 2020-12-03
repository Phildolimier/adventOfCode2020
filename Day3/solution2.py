inputFile = open("./input.txt", "r")


##how can I get the width of first line without calling inputFile.read_line()?
##in this case its fine since coord (0,0) of the first line and always NOT a tree, we can start looking on the second line.

width = len(inputFile.readline())-1

#One index in each list for each slope formula in the prompt
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
xCoords = [0,0,0,0,0]
treeCounts = [0,0,0,0,0]


line_number = 0

for line in inputFile:
    line_number += 1
    
    #check each slope where yCoord increments by 1 for slope (first 4 in prompt)
    for i in range(len(xCoords)-1):
    	xCoords[i] = (xCoords[i] + slopes[i][0]) % width
        if line[xCoords[i]] == '#':
            treeCounts[i] += 1

    #deal with last scenario separately (fifth slope in prompt)
    if line_number % 2 == 0:
        xCoords[4] = (xCoords[4] + slopes[4][0]) % width
        if line[xCoords[4]] == '#':
            treeCounts[4] += 1

for count in treeCounts:
    print(count)