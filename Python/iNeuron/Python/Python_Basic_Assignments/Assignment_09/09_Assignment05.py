import os
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		13. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?""")


def main():

	print("""Answer-
		For C:\bacon\eggs\spam.txt
		The dir name is C:\\bacon\\eggs
		The Base name is spam.txt""")

	path = r'C:\bacon\eggs\spam.txt'
	print(os.path.dirname(path))
	print(os.path.basename(path))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
