# Return Something to Me!

def function(value):
	formula = '"Something' + ' ' + value
	return formula


def main():
	sent = str(input("Enter any thing: "))

	total = function(sent)
	print("Give me", total)


if __name__ == "__main__":
	main()
