print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		6. After running the following code, what does the variable bacon contain?""")


def main():

	print("""Answer-
		The variable bacon is set to value of 22. But expression bacon + 1 does not reassign the value in bacon"
		that would the case if the expression is like 'bacon += 1' instead of 'bacon + 1'.""")

	bacon = 22
	bacon + 1                       # It may be: 'var = bacon + 1'
	print(bacon)                    # print(var)

	bacon = 22
	bacon += 1
	print(bacon)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
