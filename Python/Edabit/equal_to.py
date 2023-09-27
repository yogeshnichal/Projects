def function(x):
	equal = bool(x == 7)
	return equal

def main():
	print("Enter the number: ")
	num1 = int(input())

	fix = function(num1)
	print("Fix the code: ",fix)

if __name__ == "__main__":
	main()
