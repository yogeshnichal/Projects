print("Return the first element in a list")

def list(value1, value2, value3):
	ans = (["Mango", "Apple", "Orange"])
	return ans

def main():
	print("Enter first value: ")
	num1 = input()
	print("Enter second value: ")
	num2 = input()
	print("Enter third value: ")
	num3 = input()

	List = list(num1,num2,num3)
	print("First Element: ",List[1])

if __name__ == "__main__":
	main()
