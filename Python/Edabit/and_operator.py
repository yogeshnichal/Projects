def function(value1, value2):
	formula = value1 and value2
	return formula


def main():
	print("Enter the first value: ")
	a = str(input())
	print("Enter the second value: ")
	b = str(input())

	total = function(a, b)
	print("Checked:",total)

if __name__ == "__main__":
	main()
