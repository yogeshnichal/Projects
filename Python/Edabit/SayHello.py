def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		word = input("Enter Name: ")
		if word in '':
			print("''")
		else:
			lst.append("Hello"+' '+word)
	name = ", ".join(lst)

	print("Greet people:", name)


if __name__ == "__main__":
	main()

# def hello(value):
# 	formula = value.append("Hello" + ' ' + value)
# 	return formula
#
# 	def main():
# 		lst = []
# 		size = int(input("Enter size of list: "))
#
# 		for i in range(0, size):
# 			word = input("Enter Name: ")
#
# 	fix = hello(lst)
#
# 	print("Greet people:", fix)
#
# 	if __name__ == "__main__":
# 		main()