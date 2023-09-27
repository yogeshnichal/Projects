print("Boolean To String Conversion")

def Bool(word):
	formula = str(bool(word <=0))
	return formula

def main():
	print("Type anything: ")
	sen = float(input())
	
	ans = Bool(sen)
	print('bool_to_string :',ans)
	print(type(ans))

if __name__ == "__main__":
	main()
