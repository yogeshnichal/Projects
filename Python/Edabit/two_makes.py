def function(value1, value2):
	formula = bool(value1 + value2 ==10 or value1==10 or value2 ==10)
	return formula


def main():
	print("Enter the first value: ")
	num1 = int(input())
	print("enter the second value: ")
	num2 = int(input())

	total = function(num1, num2)
	print("Makes 10:",total)


if __name__ == "__main__":

	main()
