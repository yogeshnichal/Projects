def function(value):
	formula = value
	return formula


def main():
	lst = list()
	size = int(input("Enter the size of list: "))

	for i in range(0, size):
		num = input("Enter list: ")
		lst.append(num + '7')

	fix = function(lst)
	print("Jazzify:", str(fix))


if __name__ == "__main__":
	main()
