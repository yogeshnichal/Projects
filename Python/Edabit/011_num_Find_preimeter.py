# Find the Perimeter of a rectangle

def function(value1, value2):
	formula = (value1*2) + (value2*2)
	return formula


def main():
	num1 = int(input("Enter the first value: "))
	num2 = int(input("Enter the first value: "))

	total = function(num1, num2)
	print("Find perimeter:", total)


if __name__ == "__main__":
	main()
