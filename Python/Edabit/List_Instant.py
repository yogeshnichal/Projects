def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter the total size of list items: "))
	for i in range(0, size):
		num = input("Enter list: ")
		if num.endswith('0'):
			print()
		elif num:
			count.append(num + "7")

	fix = function(count)
	print(count)


if __name__ == "__main__":
	main()
