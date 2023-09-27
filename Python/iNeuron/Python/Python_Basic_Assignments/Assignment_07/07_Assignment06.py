import re
print("-------------------------------------Yogesh Prabhu Nichal------------------------------------------\n")
print("""Question-
		6. In standard expression syntax, parentheses and intervals have distinct meanings.
		How can you tell a regex that you want it to fit real parentheses and periods?""")


def main():

	print("""Answer-
		Periods and parentheses can be escaped with a backslash:\"""")

	PhNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
	Mob = PhNumRegex.search('My phone number is (110) 000-0022.')
	print("\t   ", Mob.group())

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
