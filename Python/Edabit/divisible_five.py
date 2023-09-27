def function(value):
	formula = bool(value % 5 ==0)
	return formula

def main():
	print("Enter the value: ")
	num1 = float(input())

	total = function(num1)
	print("Divisible by five:",total)


if __name__ == "__main__":
	main()
