# Find the Largest Number in a list

def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter the total number in list: "))

	for i in range(0, size):
		num = int(input("Enter any number: "))
		count.append(num)

	fix = function(count)
	print(count)
	print("Largest Number is:", max(count))


if __name__ == "__main__":
	main()
