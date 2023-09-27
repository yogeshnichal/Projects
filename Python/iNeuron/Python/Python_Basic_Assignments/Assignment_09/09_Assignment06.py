print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		6. What are the three mode arguments that can be passed to the open() function?""")


def main():

	print("""Answer-
		The string 'r' for read mode, 'w' for write mode, and 'a' for append mode.
		open(filename, mode)\n
		
		‘r’ – Read Mode: This is the default mode for open(). The file is opened and a pointer is positioned at the
		beginning of the file’s content.
		
		‘w’ – Write Mode: Using this mode will overwrite any existing content in a file. If the given file does not exist,
		a new one will be created.
		
		‘r+’ – Read/Write Mode: Use this mode if you need to simultaneously read and write to a file.
		
		‘a’ – Append Mode: With this mode the user can append the data without overwriting any already existing data
		in the file.
		
		‘a+’ – Append and Read Mode: In this mode you can read and append the data without overwriting the original file.
		
		‘x’ – Exclusive Creating Mode: This mode is for the sole purpose of creating new files. Use this mode if you
		know the file to be written does’t exist beforehand.""")

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
