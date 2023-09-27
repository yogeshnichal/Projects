def main():
	fruit = list()
	size = int(input("Enter total fruits number: "))

	for i in range(0, size):
		num = input("Enter Fruits Name: ")
		fruit.append(num)

	print("Fruits List:", fruit)


if __name__ == "__main__":
	main()
