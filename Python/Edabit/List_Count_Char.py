# Characters in Shapes

def function(value):
	formula = value
	return formula


def main():
	lst = list()
	size = int(input("Enter the size of list: "))

	for i in range(0,size):
		num =str(input("Enter list: "))
		if num == '':
			if num == (','):
				print(0)
		else:
			lst.append(len(num))
	print(sum(lst))

	fix = function(lst)

if __name__ == "__main__":
	main()
