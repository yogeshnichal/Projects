# Unpacking Lists

def function(value):
	formula = value
	return formula


def main():
	lst = list()
	size = int(input("Enter the total size of list number: "))

	for i in range(0, size):
		num = int(input("Enter the list: "))
		lst.append(num)

	fix = function(lst)
	print("First =", lst[0],'\n'"Middle =", lst[1:-1],'\n'"Last =", lst[-1])


if __name__ == "__main__":
	main()
