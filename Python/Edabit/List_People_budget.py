def function(value):
	formula = value
	return formula


def main():
	lst = {}
	size = int(input("Enter the size of list: "))

	for i in range(size):
		num1 = input("Name: ")
		num2 = input("Age: ")
		num3 = int(input("Budget: "))
		lst["Name"] = num1
		lst["Age"] = num2
		lst["Budget"] = num3

	fix = function(lst)
	print("Get Budgets:", fix)


if __name__ == "__main__":
	main()
