# Filter out String from an Array

def function(value):
	formula = value
	return formula

def main():
	count = list()
	size = int(input("Enter the total size of list items: "))

	for i in range(0, size):
		num = input("Enter anything: ")
		if num.isdigit():
			count.append(num)

	fix = function(count)
	print(fix)


if __name__ == "__main__":
	main()
