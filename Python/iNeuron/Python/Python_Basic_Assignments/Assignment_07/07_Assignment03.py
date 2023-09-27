import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		3. What is the return value of the search() method?""")


def main():

	print("""Answer-
		The return value of re.search() method is a match object if the pattern is observed in the string
		else it returns a None\n""")

	data = "This is iNeuron Full Stack Data Science Class"
	Pattern = re.search("i", data)

	print("The first i character is located in position:", Pattern.start())
	print(type(Pattern))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
