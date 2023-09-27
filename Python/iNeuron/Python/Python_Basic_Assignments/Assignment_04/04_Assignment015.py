print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		15. How do you get a list value's tuple form? How do you get a tuple value's list form?""")


def main():

	print("""Answer-
		The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa.\n""")

	Lst = ["Yogesh", "Amol", "Dipak"]
	Tup = tuple(Lst)
	print("\t   ", Tup)
	print("\t   ", type(Tup))

	Tup = ("Yogesh", "Amol", "Dipak")
	Lst = list(Tup)
	print("\n\t   ", Lst)
	print("\t   ", type(Lst))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
