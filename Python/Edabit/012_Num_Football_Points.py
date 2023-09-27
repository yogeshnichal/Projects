# Football Points

def function(wins, draws, losses):
	formula = (wins*3) + (draws*1) + (losses*0)
	return formula


def main():
	num1 = int(input("Enter the wins: "))
	num2 = int(input("Enter the draws: "))
	num3 = int(input("Enter the losses: "))

	total = function(num1, num2, num3)
	print("Football Points:", total)


if __name__ == "__main__":
	main()
