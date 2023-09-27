def function(*value):
	formula = sum([i[0] * i[1] * i[2] for i in value])
	return formula


def main():
	lst1 = []
	lst2 = []
	lst3 = []

	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num1 = int(input("Enter list num1: "))
		lst1.append(int(num1))

	for i in range(0, size):
		num2 = int(input("Enter list num2: "))
		lst2.append(int(num2))

	for i in range(0, size):
		num3 = int(input("Enter list num3: "))
		lst3.append(int(num3))

	total = function(lst1, lst2, lst3)

	print("Total:", total)


if __name__ == "__main__":
	main()
