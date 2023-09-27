def function(value):
	formula = value
	return formula


def main():
	lst = list()

	size = int(input("Enter the size of list: "))

	for i in range(0, size):
		num = input("Enter list: ")
		if num.isdigit():
			lst.append(num)

	fix = function(lst)

	print("Filter list:", fix)

if __name__ == "__main__":
	main()
