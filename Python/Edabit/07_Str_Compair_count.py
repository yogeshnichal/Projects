# Compair String by Count of Characters

def function(word1, word2):
	format = len(word1) == len(word2)
	return format


def main():
	sent1 = input("Enter anything: ") 
	sent2 = input("Enter anything: ") 

	nxt = function(sent1, sent2)
	print("Compair:", nxt)


if __name__ == "__main__":
	main()
