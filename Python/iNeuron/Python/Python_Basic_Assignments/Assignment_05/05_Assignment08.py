print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		8. How do you 'pretty print' dictionary values using which modules and function?""")


def main():

	print("""Answer-
		we can pretty print a dictionary using three functions

		1. by using pprint() function of pprint module
			Note: pprint() function doesn't prettify nested dictionaries
		2. by using dumps() method of json module
		3. by using dumps() method of yaml module""")
	ndict = [
		{'Name': 'Yogesh', 'Age': '33', 'Residence': {'Country': 'India', 'City': 'Nanded'}},
		{'Name': 'Amol', 'Age': '32', 'Residence': {'Country': 'India', 'City': 'Beed'}},
		{'Name': 'Dipak', 'Age': '31', 'Residence': {'Country': 'India', 'City': 'Nandurbar'}}
	]

	print('Printing using print() function\n', ndict)
	print('-'*70)
	import pprint
	print('Printing using pprint() function')
	pprint.pprint(ndict)
	print('-'*70)
	import json
	dump = json.dumps(ndict, indent=4)
	print('Printing using dumps() method\n', dump)
	print('-'*70)
	import yaml
	dump = yaml.dump(ndict)
	print('Printing using dump() method\n', dump)

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
