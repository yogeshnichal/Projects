import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		11. What is the difference between {4} and {4,5} in regular expression?""")


def main():

	print("""Answer-
		{4} means that its preceding group should repeat 4 times. where as {4,5} means that its preceding group
		should repeat minimum 4 times and maximum 5 times inclusively\n""")

	HelloRegex = re.compile(r'(Hello){3}')
	Per1 = HelloRegex.search('HelloHelloHello')
	Per2 = HelloRegex.search('Hello')
	print("\t   ", Per1.group())
	print("\t   ", Per2)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
