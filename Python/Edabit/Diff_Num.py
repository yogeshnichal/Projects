def numbers(value1, value2, value3, value4, value5, value6, value7, value8):
	function = [value1, value2, value3, value4, value5, value6, value7, value8]
	return function


def main():
	print("Enter the First number: ")
	num1 = int(input())
	print("Enter the Second number: ")
	num2 = int(input())
	print("Enter the Third number: ")
	num3 = int(input())
	print("Enter the Forth number: ")
	num4 = int(input())
	print("Enter the fifth number: ")
	num5 = int(input())
	print("Enter the sixth number: ")
	num6 = int(input())
	print("Enter the seventh number: ")
	num7 = int(input())
	print("Enter the eighth number: ")
	num8 = int(input())

	total = numbers(num1, num2, num3, num4, num5, num6, num7, num8)
	print("Biggest number is: ",max(total))
	print("Smallest number is: ",min(total))
	print("Total addition is: ", sum(total))


if __name__ == "__main__":
	main()
