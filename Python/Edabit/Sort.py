def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		if num not in lst:
			lst.append(num)

	lst.sort()
	print(lst)


if __name__ == "__main__":
	main()
