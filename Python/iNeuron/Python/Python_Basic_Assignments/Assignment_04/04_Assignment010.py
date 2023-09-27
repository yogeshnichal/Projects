print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		10. What is the difference between the list method append() and insert()?""")


def main():

	print("""Answer-
		While append() will add values only to the end of a list, insert() can add them anywhere in the list.""")
	lst = [1, 2, 3, 4, 5]
	lst.append(6)
	print("\t   ", lst)
	lst.insert(2, 'Demo')
	print("\t   ", lst)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
