# Are the Numbers Equal?

def function(value1, value2):
	formula = value1 == value2
	return formula


def main():
	num1 = input("Enter the value: ")
	num2 = input("Enter the value: ")


	total = function(num1, num2)
	print("Is same numbers:", total)


if __name__ == "__main__":
	main()
