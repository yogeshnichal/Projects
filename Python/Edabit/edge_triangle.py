print("Demonstration of edge of triangle")

def triangle(side1,side2):
	ans = (side1 + side2) - 1
	return ans

def main():
	print("Third edge :")
	num1 = int(input())

	print("Third edge :")
	num2 = int(input())

	sum = triangle(num1,num2)
	print("Maximum edge of triangle is: ",sum)

if __name__ == "__main__":
	main()
