def function(value1, value2, value3):
	formula = value1 + value2 + value3
	return formula


def main():
	print("Enter the first value: ")
	num1 = float(input())
	print("Enter the second value: ")
	num2 = float(input())
	print("Enter the third value: ")
	num3 = float(input())

	total = function(num1, num2, num3)
	print("List:",[num1,num2,num3])
	print("Get sum of elements",int(total))


if __name__ == "__main__":
	main()