print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		8. Why is eggs a valid variable name while 100 is invalid?""")

def main():

	print("""Answer-
		As per Python naming rules Variable names cannot began with a number.\n.""")

	egg = "iNeuron"  # valid variable initialization
	print(egg)  # value of egg is iNeuron
	# 100 = 'Hello'  # invalid variable initialization
	# print(100)  # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

	print("""Python Naming Rules:-
1. Variable name must start with a letter or the underscore character.
2. Variable name cannot start with a number.
3. Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
4. Variable names are case-sensitive (INeuron, INEURON and ineuron are three different variables).
5. The reserved words(keywords) cannot be used naming the variable.""")

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
