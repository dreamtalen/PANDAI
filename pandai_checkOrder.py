if __name__ == '__main__':
	inputFile = open('1.txt')
	checkFile = open('2.txt')
	resultFile = open('result.txt', 'w')
	inputList = inputFile.read().split()
	checkList = checkFile.read().split()
	for i in inputList:
		if i not in checkList:
			resultFile.write(i)
			resultFile.write('\n')

