print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		4. What happens if you try to access spam ['foo'] if spam is {'bar':100}?""")


def main():

	print("""Answer-
		We will get a keyError KeyError: 'foo'""")

	spam = {'bar': 100}							# 'bar' it's key value
	print("\t   ", "spam:", spam['foo'])		# 'foo' it's not key value

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
