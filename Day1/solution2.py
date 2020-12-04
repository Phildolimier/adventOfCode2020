inputFile = open("./input.txt", "r")

hash = {}
nums = []

for element in inputFile:
    hash[int(element)] = int(element)
    nums.append(int(element))



for i in range(len(nums)):
    for j in range(i, len(nums)):
	if 2020 - (nums[i]+nums[j]) in hash:
		print(nums[i],nums[j], 2020-(nums[i]+nums[j]))
		break;
	
