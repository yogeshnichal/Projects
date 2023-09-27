import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
		return?""")


def main():

	print("""Answer-
		The Output will be 'X drummers, X pipers, five rings, X hen'.\n""")
	numReg = re.compile(r'\d+')
	print("\t   ", numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen'))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
