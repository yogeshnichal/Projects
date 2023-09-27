print("-------------------------------------Yogesh Prabhu Nichal------------------------------------------\n")
print("""Question-
		2. In a list of values stored in a variable called spam, how would you assign the value 'hello'
		as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)""")


def main():

	print("""Answer-
		spam[2]='hello'\n""")

	spam = [2, 4, 6, 8, 10]
	print("\t   ", spam)
	spam[2] = 'hello' 		# List uses zero based indexing
	print("\t   ", spam)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
