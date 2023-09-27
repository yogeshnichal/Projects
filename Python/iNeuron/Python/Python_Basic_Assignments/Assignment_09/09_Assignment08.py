print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		8. How do you tell the difference between read() and readlines()?""")


def main():

	print("""Answer-
		The main difference is that read() will read the whole file at once and then print out the first characters that
		take up as many bytes as you specify in the parenthesis

		Whereas the readline() that will read and print out only the first characters that take up as many bytes as you
		specify in the parenthesis. You may want to use readline() when you're reading files that are too big for your RAM.
		
		The read() would treat each character in the file separately, meaning that the iteration would happen for every character.
		
		The readline() function, on the other hand, only reads a single line of the file. This means that if the first
		line of the file were three lines long, the readline() function would only parse (or iterate/operate) on the first
		line of the file.""")

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
