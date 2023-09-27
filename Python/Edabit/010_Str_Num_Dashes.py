# Convert Number to String of Dashes

def function(value):
	formula = value * "-"
	return formula


def main():
	num = int(input("Enter any number: "))
	fix = function(num)
	print("Convert number to dash:", fix)
	print(type(fix))


if __name__ == "__main__":
	main()
