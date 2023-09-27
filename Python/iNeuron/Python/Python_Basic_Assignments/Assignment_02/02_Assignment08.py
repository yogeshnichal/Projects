print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam,
		and prints Greetings! if anything else is stored in spam?""")


def spamCode(spam):
	if spam == 1:
		print('Hello')
	elif spam == 2:
		print('Howdy')
	else:
		print('Greetings')


def main():
	spamCode(1)
	spamCode(2)
	spamCode(3)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
