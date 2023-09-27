def function(value1, value2):
	formula = value1 == value2 ** value2
	return formula


def main():
	print("Enter the first value: ")
	num1 = int(input())
	print("Enter the second value: ")
	num2 = int(input())

	total = function(num1, num2)
	print("K to K:",total)

if __name__ == "__main__":
	main()
