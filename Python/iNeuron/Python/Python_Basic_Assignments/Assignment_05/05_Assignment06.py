print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
		'cat' in spam.values()?""")


def main():

	print("""Answer-
		'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values()
		checks whether there is a value 'cat' for one of the keys in spam.""")

	spam = {'a': 1, 'b': 2, 'cat': 3, 'd': 4}
	print("\t   ", "cat" in spam)
	print("\t   ", "cat" in spam.values())

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
