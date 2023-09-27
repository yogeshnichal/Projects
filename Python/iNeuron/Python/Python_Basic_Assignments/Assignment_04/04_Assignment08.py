print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		8. How does bacon.remove('cat') change the look of the list in bacon?""")


def main():

	print("""Answer-
		The remove method removes the first occurrence of the element in the list.""")
	bacon = [3.14, 'cat', 11, 'cat', True]
	print("\t   ", bacon)
	bacon.remove("cat")		# first occurrence of the element in the list
	print("\t   ", bacon)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
