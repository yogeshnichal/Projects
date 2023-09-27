def function(value1, value2):
	if value1.isdigit() and value2:
		return "Not A String !!"
	else:
		return value1 * value2


def main():
	num1 = input("Enter the first value: ")
	num2 = int(input("Enter the second value: "))

	fix = function(num1, num2)
	print(fix)


if __name__ == "__main__":
	main()
