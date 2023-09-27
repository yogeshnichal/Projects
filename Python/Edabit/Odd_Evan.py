def function(value):
	formula = len(value)%2==0
	return formula


def main():
	print("Enter any String Value: ")
	word = str(input())


	total = function(word)
	print("Odd or Even:",total)


if __name__ == "__main__":
	main()
