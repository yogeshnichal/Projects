# Concatenating Two Integer Lists

def function(value1, value2):
	formula = value1, value2
	return formula


def main():
	count1 = list()
	size1 = int(input("Enter First List Total Number: "))
	count2 = list()
	size2 = int(input("Enter Second List Total Number: "))

	for i in range(0, size1):
		num1 = int(input("Enter First List: "))
		count1.append(num1)

	for i in range(0, size2):
		num2 = int(input("Enter Second List: "))
		count2.append(num2)

	fix = function(count1, count2)
	print("Concatenating Two Lists:", count1+count2)


if __name__ == "__main__":
	main()
