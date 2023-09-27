print("Sum of Polygon Angles")

def Sum(value1):
	formula = (value1 - 2) * 180
	return formula

def main():
	print("N side polygon is: ")
	poly = int(input())

	ans = Sum(poly)
	print("sum of internal angles is: ",ans)

if __name__ == "__main__":
	main()
