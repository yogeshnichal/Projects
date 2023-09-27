def function(value1):
	formula = ("Hello" + ' ' + value1 + "!")
	return formula


def main():
	num1 = input()

	item = function(num1)
	print(item)

if __name__ == "__main__":
	main()
