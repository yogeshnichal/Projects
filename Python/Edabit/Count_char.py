def function(value1, value2):
	formula = len(value1) == len(value2)
	return formula


def main():
	print("Enter the first value: ")
	char1 = str(input())
	print("Enter the second value: ")
	char2 = str(input())

	total = function(char1, char2)
	print("Compair:",bool(total))

if __name__ == "__main__":
	main()
