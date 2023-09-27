# Find the Odd Integer

def function(value):
	for i in value:
		if value.count(i) % 2 == 1:
			return i


def main():
	count = list()
	size = int(input("Enter total size of list: "))

	for i in range(0, size):
		num = int(input("Enter the list: "))
		count.append(num)

	fix = function(count)
	print("Find Odd:", fix)


if __name__ == "__main__":
	main()
