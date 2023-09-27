# Character in Shapes

def function(value):
	formula = value
	return formula

def main():
	count = list()
	size = int(input("Enter the total size of list items: "))

	for i in range(0, size):
		num = len(input("Enter the list: "))
		count.append(num)

	# fix = function(count)
	print("Count of Characters:", count)


if __name__ == "__main__":
	main()
