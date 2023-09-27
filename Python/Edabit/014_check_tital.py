# Check if It's a Title String

def function(word):
	formula = word.istitle()
	return formula


def main():
	sent = input("Enter any sentence: ")

	fix = function(sent)
	print("Check Title:", fix)


if __name__ == "__main__":
	main()
