# Buggy Code

def function(words):
	formula = '"Hello,' + ' ' + words + '!"'
	return formula


def main():
	sent = str(input("Enter any name: "))

	nxt = function(sent)
	print("Greeting:", nxt)


if __name__ == "__main__":
	main()
