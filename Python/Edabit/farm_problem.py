print("The Farm Problem")

def farm(chickens, cows, pigs):
	legs = chickens*2 + cows*4 + pigs*4
	return legs

def main():
	print("Total chickens: ")
	count = int(input())
	print("Total cows: ")
	count1 = int(input())
	print("Total pigs: ")

	count2 = int(input())

	Total = farm(count, count1, count2)
	print("Total animals legs: ",Total)

if __name__ == "__main__":
	main()
