def maximum(value1, value2):
	if value1 > value2:
		return value1
	else:
		return value2


def main():
	num1 = input("Enter the first number: ")
	num2 = input("Enter the second number: ")

	fix = maximum(int(num1), int(num2))
	print("Maximum number is:", fix)


if __name__ == "__main__":
	main()
