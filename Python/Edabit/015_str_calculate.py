# Calculate Using String Operation

def function(value1, value2, value3):
	if value3 == "+":
		print(value1 + value2)
	if value3 == "-":
		print(value1 - value2)
	if value3 == "*":
		print(value1 * value2)
	if value3 == "/":
		print(value1 / value2)
	if value3 == "//":
		print(value1 // value2)
	if value3 == "%":
		print(value1 % value2)
	return

def main():
	num1 = int(input("Enter first value: "))
	num2 = int(input("Enter second value: "))
	num3 = input("Enter third value: ")

	fix = function(num1, num2, num3)


if __name__ == "__main__":
	main()
