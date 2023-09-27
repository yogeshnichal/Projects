# Check String fo Spaces

def function(var):
	formula = var
	if var == var+ " ":
		print(True)
	elif var == var:
		print(False)
	return formula

def main():
	num = str(input("Enter anything:"))
	
	fix = function(num)
	print("Check Spaces:", fix)


if __name__ == "__main__":
	main()
