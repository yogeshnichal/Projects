# Return with Hello

def function(value):
	formula = "Hello" + ' ' + value
	return formula


def main():
	sent = str(input("Enter any name: "))

	total = function(sent)
	print(total)

if __name__ == "__main__":
	main()