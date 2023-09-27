def function(prob, prize, pay):
	formula = bool(prob * prize > pay)
	return formula


def main():
	print("Enter the prob value: ")
	num1 = float(input())
	print("Enter the prize value: ")
	num2 = float(input())
	print("Enter the pay value: ")
	num3 = float(input())

	total = function(num1, num2, num3)
	print("Profitable Gamble:",total)


if __name__ == "__main__":
	main()
