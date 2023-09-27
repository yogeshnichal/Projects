def numbers(value1, value2, value3, value4):
	formula = min(value1, value2, value3, value4)
	return formula


def main():
	print("Any first number: ")
	num1 = input()
	print("Any second number: ")
	num2 = input()
	print("Any third number: ")
	num3 = input()
	print("Any forth number: ")
	num4 = input()

	mini = numbers(num1, num2, num3, num4)
	print("List:",[num1, num2, num3, num4])
	print("Smallest number is: ",mini)


if __name__ == "__main__":
	main()
