def cacti_number(dArray):
	possible = 0
	rows, cols = len(dArray), len(dArray[0])
	for i in range(rows):
		adjacent = False
		for j in range(cols):
			adjacent = True
			if dArray[i][j] == 0:
				adjacent = False
				if i > 0 and dArray[i-1][j] == 1:
					adjacent = True
				elif i < rows - 1 and dArray[i+1][j] == 1:
					adjacent = True
				elif j > 0 and dArray[i][j - 1] == 1:
					adjacent = True
				elif j < cols - 1 and dArray[i][j+1] == 1:
					adjacent = True
			if not adjacent:
				possible += 1
				dArray[i][j] = 1
	print(dArray)
	return possible


DArray=[[1, 0, 1, 0, 1],[0,0,0,0,0],[1,0,0,0,0]]

print(cacti_number(DArray))

DArray = [[0,1, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0],[1,0,1,0,0,1]]
print(cacti_number(DArray))
