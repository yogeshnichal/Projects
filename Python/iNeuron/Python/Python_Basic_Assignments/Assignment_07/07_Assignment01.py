print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		1. What is the name of the feature responsible for generating Regex objects?""")


def main():

	print("""Answer-
		re.compile() the name of function which returns Regex objects.""")

	import re
	Pattern = re.compile("Regex_objects_pattern")
	print(type(Pattern))
	print(Pattern)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
