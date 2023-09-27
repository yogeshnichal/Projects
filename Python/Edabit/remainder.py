print("Return the Remainder from Two Numbers")

def divided(value1, value2):
	ans = (value1%value2)
	return ans

def main():
	print("Enter the first value: ")
	num1 = float(input())
	print("Enter the second value: ")
	num2 = float(input())

	div = divided(num1,num2)
	print("Remainder is: ",div)

if __name__ == "__main__":
	main()
