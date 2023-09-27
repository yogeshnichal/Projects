import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		7. The findall() method returns a string list or a list of string tuples.
		What causes it to return one of the two options?""")


def main():

	print("""Answer-
		If the regex has no groups, a list of strings is returned. If the regex has groups,
		a list of tuples of strings is returned.""")

	PhNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
	Mob = PhNumRegex.findall('My phone number is (110) 000-0022.')
	print("\t   ", Mob)

	PhNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
	Mob = PhNumRegex.findall('My phone number is 110-000-0022.')
	print("\t   ", Mob)			# Tuple format


print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
