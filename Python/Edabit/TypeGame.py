def function(value1, value2):
	formula = [1 if x in value1 else -1 for x in value2]
	return formula


def main():
	lst1 = []
	lst2 = []

	size = int(input("Enter list: "))

	for i in range(0, size):
		word1 = input("First list:")
		lst1.append(word1)

	for i in range(0, size):
		word2 = input("Second list:")
		lst2.append(word2)

	total = function(lst1,lst2)

	print("Output: ", total)


if __name__ == "__main__":
	main()
