def main():
	count = list()
	size = int(input("Enter in the list total number items: "))
	print("Enter the items:")

	for i in range(0, size):
		num = int(input())
		count.append(num)

	print(count)

if __name__ == "__main__":
	main()
