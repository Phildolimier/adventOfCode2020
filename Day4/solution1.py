import re
inputFile = open("./input.txt", "r")
pattern = re.compile(r'(\S+):(\S+)')

validCount = 0
hash = {}

for line in inputFile:

    if line.isspace():
	print(hash)
	#checkValidFields (either 8 entries or (7 entries and cid not in hash))
	if len(hash) == 8 or (len(hash) == 7 and "cid" not in hash):
	    #increment if valid
	    validCount += 1
	    print("valid")

	#reset hash for next passport
        hash = {}

    else:
	#re to get groups, add key,value pairs to hash
	for (key, value) in re.findall(pattern, line):
            hash[key] = value

#no ending white line

#checkValid (either 8 entries or (7 entries and cid not in hash))
	if len(hash) == 8 or (len(hash) == 7 and "cid" not in hash):
	    #increment if valid
	    validCount += 1
	    print("valid")

print(validCount)