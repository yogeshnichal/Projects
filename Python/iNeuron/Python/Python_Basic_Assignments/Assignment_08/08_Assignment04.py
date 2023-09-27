import pyinputplus as pypi
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?""")


def main():

	print("""PyInputPlus module provides a function called as inputInt() which only returns only integer values.
	inorder to restrict the input between 0 and 99, i'ii use parameters like min & max to ensure that user enters
	the values between the defined range only.""")

	whole_number = pypi.inputInt(prompt='Enter a number: ', min=0, max=100)
	print(whole_number)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
