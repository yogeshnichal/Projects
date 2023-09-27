# # Moving to the end multiple elements
# def main():
# 	lst = list()
# 	size = int(input("Enter the size of list: "))
#
# 	for i in range(size):
# 		num = input("Enter first list: ")
# 		lst.append(num)
# 	print("Original list is: ", lst)
#
# 	shift = int(input("Enter the position: "))
# 	for count in range(shift):
# 		x = lst[0]
# 		for i in range(1, size):
# 			lst[i-1] = lst [i]
# 		lst[size-1] = x
#
# 	print("Move To End:", lst)
#
#
# if __name__ == "__main__":
# 	main()


# Moving to the end single element
def main():
	lst = list()
	size = int(input("Enter the size of list: "))

	for i in range(size):
		num = input("Enter first list: ")
		lst.append(num)
	print("Original list is: ", lst)

	lst.sort(key=input("Enter the position: ").__eq__)

	print("Move To End:", str(lst))


if __name__ == "__main__":
	main()
