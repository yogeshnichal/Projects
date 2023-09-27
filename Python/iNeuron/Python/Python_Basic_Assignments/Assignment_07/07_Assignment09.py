import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		9. In regular expressions, what does the? character stand for?""")


def main():

	print("""Answer-
		In regular Expressions, characters represents zero or one match of the preceding group.""")

	Match1 = re.search("Bat(wo)?man", "Batman returns")
	print("\t   ", Match1)
	Match2 = re.search("Bat(wo)?man", "Batwoman returns")
	print("\t   ", Match2)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
