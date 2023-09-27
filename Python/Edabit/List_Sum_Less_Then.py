# Sum of List Less Than 100 List Remix

def function(value):
	formula = value
	return formula


def main():
	count = list()
	size = int(input("Enter the size of list: "))

	for i in range(0, size):
		num = int(input("Enter list numbers: "))
		count.append(num)

	fix = function(count)
	print("List total is less then 100:", sum(count) < 100)


if __name__ == "__main__":
	main()
