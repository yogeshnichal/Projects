def numbers(value1, value2):
	formula = bool(value1 + value2 < 100)
	return formula


def main():
	print("Enter the first value: ")
	num1 = int(input())
	print("Enter the second value: ")
	num2 = int(input())

	total = numbers(num1, num2)
	print("Less Then 100 is:",total)


if __name__ == "__main__":
	main()
