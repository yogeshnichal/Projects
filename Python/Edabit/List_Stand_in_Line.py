# def main():
# 	lst = list()
# 	size = int(input("Enter the total size of list items: "))
# 	for i in range(0, size):
# 		num = input("Enter list: ")
# 		if num:
# 			lst.append(num)
# 		elif print("Original list is: ", lst):
# 			lst.append(input("Enter new number: "))
# 		else:
# 			num.endswith('')
# 			print("No list has been selected")
#
# 	fix = function(lst)
# 	print(lst[1:])
#
#
# if __name__ == "__main__":
# 	main()

def function(value):
	if len(value) == 1:
		return "No list has been selected"
	else:
		return value[1:]


def main():
	lst = list()
	size = int(input("Enter the total size of list items: "))
	for i in range(0, size):
		num = input("Enter list: ")
		lst.append(num)
	lst.append(input("Enter new number: "))
	fix = function(lst)
	print("Stand in Line:", fix)


if __name__ == "__main__":
	main()
