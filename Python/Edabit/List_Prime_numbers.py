def main():
	count = list()
	size = int(input("Enter the total items in list: "))
	print("Enter the items: ")

	for i in range(10, 15):
		num = int(input())
		count.append(num)

	print("Prime numbers",count)


if __name__ == "__main__":
	main()
