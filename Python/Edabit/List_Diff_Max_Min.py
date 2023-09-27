# Difference of Max and Min Numbers in List

def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter the total numbers in list: "))

	for i in range(0, size):
		num = int(input("Enter list numbers: "))
		count.append(num)

	fix = function(count)
	print("Biggest number:", max(count))
	print("Smallest number:", min(count))
	print("Total list addition:", sum(count))


if __name__ == "__main__":
	main()
