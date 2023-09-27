print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
		'cat' in spam.keys()?""")


def main():

	print("""Answer-
		There is no difference. The operator checks whether a value exits as a key in the dictionary or not\n""")
	spam = {'a': 1, 'b': 2, 'cat': 3, 'd': 4}
	print("\t   ", "cat" in spam)
	print("\t   ", "cat" in spam.keys())

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
