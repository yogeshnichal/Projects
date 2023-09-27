import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover?
		Group 2? Group 1?""")


def main():

	print("""Answer-
		Group 0 is the entire match, group 1 covers the first set of parentheses,
		and group 2 covers the second set of parentheses.""")

	PhNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	Mob = PhNumRegex.search('My number is 110-000-0022.')
	print("\t   ", Mob.groups())		# Prints all groups in a tuple format
	print("\t   ", Mob.group())		# Always returns the fully matched string
	print("\t   ", Mob.group(1))		# Returns the first group
	print("\t   ", Mob.group(2))		# Returns the second group

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
