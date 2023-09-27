# Return the Last Element in a List

def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter anything: "))

	for i in range(0, size):
		num = input("Enter list items: ")
		count.append(num)

	fix = function(count)
	print("Last item:", count[-1])


if __name__ == "__main__":
	main()
