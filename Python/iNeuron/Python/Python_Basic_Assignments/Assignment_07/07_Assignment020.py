import re
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		20. How would you write a regex that match a number with comma for every three digits? It must match the given following:

		'42'
		'1,234'
		'6,368,745'
		but not the following:
		'12,34,567' (which has only two digits between the commas)
		'1234' (which lacks commas)""")


def main():

	print("""Answer-
		re.compile(r'^\d{1,3}(,\d{3})*$') will create this regex, but other regex strings can produce a similar
		regular expression.""")

	Pattern = r'^\d{1,3}(,\d{3})*$'
	Reg = re.compile(Pattern)
	for ele in ['42', '1,234', '6,368,745', '12,34,567', '1234']:
		print('Output:', ele, "=", Reg.search(ele))

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
