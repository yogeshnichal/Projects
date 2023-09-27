def main():
	lst1 = []
	lst2 = []

	size = int(input("Enter size of list"))

	for i in range(0, size):
		num1 = int(input("Enter First list:"))
		lst1.append(num1)

	for i in range(0, size):
		num2 = int(input("Enter Second list:"))
		lst2.append(num2)
	if lst1[:-1] == lst2[1:]:
		print(True)
	else:
		print(False)
	print("Simon_Says:", lst1, lst2)


if __name__ == "__main__":
	main()
