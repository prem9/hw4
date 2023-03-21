def merge(theList1, theList2):
	x = 0
	y = 0
	newList = []
	while len(theList1) > x or len(theList2) > y:
		if  len(theList1) <= x:
			newList.append(theList2[y])
			y = y + 1
		elif len(theList2) <= y:
			newList.append(theList1[x])
			x = x + 1
		else:
			if theList1[x] > theList2[y]:
				newList.append(theList2[y])
				y = y + 1
			else:
				newList.append(theList1[x])
				x = x + 1
	return newList
