def palindrome(thatList):
	if len(thatList) % 2 == 0:
		for x in range(len(thatList)//2):
			print(thatList[x])
			if thatList[x] == thatList[-(x+1)]:
				nothing = 0
			else:
				return False

		return True
	else:
		for x in range((len(thatList)//2)):
			if thatList[x] == thatList[-(x+1)]:
				nothing = 0
			else:
				return False
		return True
