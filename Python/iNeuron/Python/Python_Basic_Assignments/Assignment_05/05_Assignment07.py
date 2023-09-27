print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		7. What is a shortcut for the following code?
		if 'color' not in spam: spam['color'] ='black'""")


def main():

	print("""Answer-
		The append method adds new elements to the end of the list.\n""")

	spam = {'a': 1, 'b': 2, 'cat': 3, 'd': 4}
	# if 'color' not in spam:
	# 	spam['color'] = 'black'
	#
	# 	"instead"

	spam = {'a': 1, 'b': 2, 'cat': 3, 'd': 4}
	spam.setdefault("color", "black")

	print("\t   ", spam['color'])

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
