def society_name(value):
	name = ""
	value.sort()
	for i in value:
		name += i[0]
	return name

def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = input("Enter list: ")
		lst.append(num)

	fix = society_name(lst)
	print("Society_Name:", fix)


if __name__ == "__main__":
	main()


# def main():
# 	lst = []
# 	size = int(input("Enter size of list: "))
#
# 	for i in range(0, size):
# 		num = input("Enter list: ")
# 		lst.append(num)
# 	name = ''
# 	lst.sort()
# 	for i in lst:
# 		name += i[0]
# 	print(name)
#
#
# if __name__ == "__main__":
# 	main()
