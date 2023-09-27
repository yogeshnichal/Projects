print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		12. Write a short program that prints the numbers 1 to 10 using a for loop.
		Then write an equivalent program that prints the numbers 1 to 10 using a while loop?""")


def main():

	print('-'*10, 'Using For Loop', '-'*10)
	for i in range(1, 11):
		print(i, end=" ")
	print('\n')
	print('-'*10, 'Using While Loop', '-'*10)
	i = 1
	while i <= 10:
		print(i, end=" ")
		i += 1

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
