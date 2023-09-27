# Burrrrp

def function(value):
	formula = "Bu" + 'r' * value + "p"
	return formula
	

def main():
	num = int(input("Enter any value: "))

	fix = function(num)
	print("Long Burp:", fix)


if __name__ == "__main__":
	main()