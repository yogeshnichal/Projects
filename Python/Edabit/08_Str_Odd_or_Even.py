# Is the String Odd or Even?

def function(value):
	format = len(value) % 2 == 0
	return format


def main():
	word = input("Enter anything: ")
	
	nxt = function(word)
	print("Odd or Even:", nxt)


if __name__ == "__main__":
	main()
