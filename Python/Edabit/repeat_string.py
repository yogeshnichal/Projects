def function(value1, value2):
	formula = value1 * value2
	return formula


def main():
	print("Enter any string value: ")
	char1 = str(input())
	print("Enter any Integer value: ")
	num1 = int(input())


	total = function(char1, num1)
	print("String Repetition:",total)


if __name__ == "__main__":
	main()
