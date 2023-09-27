# Front 3 Slice Check Repeat Concatenate

def function(word):
	formula = (word[0:3]*3)
	return formula


def main():
	sent = input("Enter any word: ")

	total = function(sent)
	print("Front 3 Characters:", total)


if __name__ == "__main__":
	main()
