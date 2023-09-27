import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

		'Haruto Watanabe'
		'Alice Watanabe'
		'RoboCop Watanabe'
		
		but not the following:
		
		'haruto Watanabe' (where the first name is not capitalized)
		'Mr. Watanabe' (where the preceding word has a nonletter character)
		'Watanabe' (which has no first name)
		'Haruto watanabe' (where Watanabe is not capitalized)""")


def main():

	print("""Answer-
		re.compile(r'[A-Z][a-z]*\sWatanabe').""")

	Pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
	Reg = re.compile(Pattern)
	for name in ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']:
		print('Output: ', name, "=", Reg.search(name))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
