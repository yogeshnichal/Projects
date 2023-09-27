# Word without First Character

def function(word):
	formula = word [1:]
	return formula


def main():
	sent = input("Enter any word: ")

	fix = function(sent)
	print("New Word:",fix)

if __name__ == "__main__":

	main()
