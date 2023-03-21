def sort_dictionary(theDict):
	newDict = sorted(theDict.items(), key = lambda x:x[1][1])
	print(newDict)
	outList = []
	for item in newDict:
		tuple2 = (item[0], item[1][0])
		outList.append(tuple2)
