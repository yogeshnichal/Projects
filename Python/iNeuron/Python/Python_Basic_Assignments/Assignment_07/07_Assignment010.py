import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		10. In regular expressions, what is the difference between the + and * characters?""")


def main():

	print("""Answer-
		In Regular Expressions, * Represents Zero ore more occurrences of the preceding group,
		whereas + represents one or more occurrences of the preceding group.""")

	Match1 = re.search("Bat(wo)*man", "Batman returns")
	print("\t   ", Match1)
	Match2 = re.search("Bat(wo)+man", "Batman returns")
	print("\t   ", Match2)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
