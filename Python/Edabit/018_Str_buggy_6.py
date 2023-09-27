def function(value):
	formula = "".join(char for char in value if not char.isdigit())
	return formula


def main():
	var = input("Enter the input:")
	
	fix = function(var)
	print("Remove Number:", fix)

if __name__ == "__main__":
	main()
