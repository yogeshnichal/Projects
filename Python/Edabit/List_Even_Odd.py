def function(value):
	formula = value
	if sum(value) % 2 == 0:
		print("even")
	else:
		print("odd")
	return formula


def main():
	count = list()
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter any number: "))
		count.append(num)

	fix = function(count)


if __name__ == "__main__":
	main()
