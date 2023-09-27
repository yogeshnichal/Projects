# Moving to the End

def function(value):
	formula = value
	return formula


def main():
	lst = list()
	size = int(input("Enter the size of list: "))

	for i in range(0, size):
		num = input("Enter List: ")
		lst.append(num)
	lst.sort(key=input("Enter move to End: ").__eq__)

	fix = function(lst)
	print("Move to end:", fix)


if __name__ == "__main__":
	main()
