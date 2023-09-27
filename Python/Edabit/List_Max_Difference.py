# Maximum Difference

def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter the size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		count.append(num)

	fix = function(count)
	print(count)
	print("Difference:", max(count) - min(count))


if __name__ == "__main__":
	main()
