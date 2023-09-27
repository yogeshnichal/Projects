def main():
	lst = []
	size = int(input("Enter size of list"))

	first = int(input("Enter first of list"))
	mid = int(input("Enter mid of list"))
	last = int(input("Enter last of list"))
	
	for i in range(first, mid, last):
		num = int(input("Enter number: "))
		lst.append(num)

	print(lst)


if __name__ == "__main__":
	main()
