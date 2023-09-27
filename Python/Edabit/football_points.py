print("Football points")

def points(value1, value2, value3):
	formula = value1*3 + value2*1 + value3*0
	return formula

def main():
	print("football matches win points: ")
	wins = int(input())
	print("football matches draws points: ")
	draws = int(input())
	print("football matches losses points: ")

	losses = int(input())
	total = points(wins,draws,losses)
	print("Total Points: ",total)

if __name__ == "__main__":
	main()
