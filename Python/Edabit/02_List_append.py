def main():
	count = list()
	size = int(input("Enter the total fruits items number:"))
	print("Enter the fruits name:")

	for i in range(0, size):
		fruit = str(input())
		count.append(fruit)

	print("Fruit list:", count)

if __name__ == "__main__":
	main()
