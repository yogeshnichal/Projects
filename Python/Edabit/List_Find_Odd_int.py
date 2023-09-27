# Find the odd integer

def function(value):
	formula = value
	for i in value:
		if value.count(i) % 2 != 0:
			return i


def main():
	lst = list()
	size = int(input("Enter the size of list: "))

	for i in range(size):
		num = int(input("Enter list: "))
		lst.append(num)

	fix = function(lst)
	print("Find odd:", fix)


if __name__ == "__main__":
	main()
