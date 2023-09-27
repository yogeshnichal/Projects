def main():
	count = list()
	element = int(input("Enter List Element: "))

	for i in range(0, element):
		value = int(input("Enter number: "))
		count.append(value)

	print("Get First Element:", count[0])

if __name__ == "__main__":
	main()
