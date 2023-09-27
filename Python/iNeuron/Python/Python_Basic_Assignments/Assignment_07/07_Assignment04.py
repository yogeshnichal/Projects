import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		4. From a Match item, how do you get the actual strings that match the pattern?""")


def main():

	print("""Answer-
		The group() method returns strings of the matched text.""")

	match = re.search('iNeuron', 'iNeuron Full Stack Data Science 2.0', flags=re.IGNORECASE)
	print('Output:', match.group())

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
