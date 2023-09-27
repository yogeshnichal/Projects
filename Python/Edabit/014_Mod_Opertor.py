# Proper Modulo Operator

def function(value1, value2):
	formula = value1 % value2
	return formula


def main():
	num1 = int(input("Enter any number: "))
	num2 = int(input("Enter any number: "))

	total = function(num1, num2)
	print("Modulo:", total)


if __name__ == "__main__":
	main()
