# Boolean to String Conversion

def function(value1, value2):
	formula = str(bool(value1 == value2))
	return formula
	
	
def main():
	num1 = str(input("Enter the value: "))
	num2 = str(input("Enter the value: "))

	nxt = function(num1,num2)
	print("Boolean to String:", nxt)
	print(type(nxt))


if __name__ == "__main__":
	main()
