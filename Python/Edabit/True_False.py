def function(value):
	formula = value
	return formula


def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		if num == 0:
			lst.append(bool(num))
		elif num == 1:
			lst.append(bool(num))


	total = function(lst)
	print("boolean:", total)


if __name__ == "__main__":
	main()
