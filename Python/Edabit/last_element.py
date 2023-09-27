def function(value1, value2, value3):
	formula = (value1, value2, value3)
	return formula


def main():
	print("Enter anything: ")
	item1 = input()
	print("Enter anything: ")
	item2 = input()
	print("Enter anything: ")
	item3 = input()
	
	total = function(item1, item2, item3)
	print("List:", item1, item2, item3)
	print("Get Last Item:", total[-1])


if __name__ == "__main__":
	main()
