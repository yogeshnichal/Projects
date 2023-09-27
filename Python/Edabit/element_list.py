print("Return the first element in a list")

def list(value1, value2, value3):
	ans = ([value1])
	return ans

def main():
	print("Enter first value: ")
	num1 = int(input())
	print("Enter second value: ")
	num2 = int(input())
	print("Enter third value: ")
	num3 = int(input())

	List = list(num1,num2,num3)
	print("First Element: ",List)

if __name__ == "__main__":
	main()
