# WordCharWord

def function(word1, word2):
	formula = word1.replace(" ", word2)
	return formula


def main():
	sent1 = input("Enter anything: ")
	sent2 = input("Enter anything: ")


	fix = function(sent1,sent2)
	print("Add:", fix)


if __name__ == "__main__":
	main()

