# Is the Word Singular or Plural?

def function(word):
	formula = (word[-1] == "s")
	return formula


def main():
	sent = input("Enter the singular or plural word: ")

	fix = function(sent)
	print("Is Plural:", fix)

if __name__ == "__main__":
	main()
