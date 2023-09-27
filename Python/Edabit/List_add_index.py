def function(value):
	formula = value
	return formula
	# index = 0
	# lst1 = list()
	# for i in value:
	# 	lst1.append(i + index)
	# 	index += 1
	# return lst1


def main():
	lst = list()
	size = int(input("Enter the size of list: "))
	index = 0
	for i in range(0, size):
		num = int(input("Enter the number: "))
		lst.append(num+index)
		index +=1

	fix = function(lst)
	print("add indexes:", fix)


if __name__ == "__main__":
	main()
