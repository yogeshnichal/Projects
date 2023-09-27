print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		9. What three functions can be used to get the integer,floating-point number,or string version of a value?""")


def main():

	print("""Answer-
		These function we can use int() for integer, float() for floating point and str() for string version value.""")

	A = 5.5
	B = 5
	C = 5

	# Explicit type casting
	a = int(A)
	b = float(B)
	c = str(C)

	print("A -> ", a)                   # int() function converts given input to int
	print("Before: ", type(A))
	print("After: ", type(a), "\n")

	print("B -> ", float(B))            # float() function converts given input to float
	print("Before: ", type(B))
	print("After: ", type(b), "\n")

	print("C -> ", str(C))              # str() function converts given input to string
	print("Before: ", type(C))
	print("After: ", type(c))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
