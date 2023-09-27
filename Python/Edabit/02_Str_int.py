# Return a String as na Integer

def function(value):
	formula = int(value)
	return formula


def main():
	num = str(input("Enter any number: "))

	nxt = function(num)
	print("String to Integer:", nxt)
	print(type(nxt))


if __name__ == "__main__":
	main()
