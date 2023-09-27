def main():
	lst = []
	size = int(input("Enter size of list: "))
	
	for i in range(size):
		num = int(input("Enter list: "))
		lst.append(num)

	print("Clone:", lst.__add__([lst]))


if __name__ == "__main__":
	main()
