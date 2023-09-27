def function(value):
	formula = value
	if formula > 0:
		print(-formula)
	elif formula <= 0:
		print(formula)
	return formula


def main():
	num = int(input("Enter the value: "))
	# if num > 0:
	# 	print(-num)
	# elif num <= 0:
	# 	print(num)

	total = function(num)


if __name__ == "__main__":
	main()
