def Objects(Value1, Value2):
	formula = Value1 == Value2
	return formula

def main():
	Obj1 = {
	"name": "Benny",
	"phone": "8888676824",
	"email": "myfriend.nichal@gmail.com"
	}

# The Second Object Parameter.

	Obj2 = {
	"name": "Jason",
	"phone": "8983634588",
	"email": "myfriend1.nichal@gmail.com"
	}

	Is_Equal = Objects(Obj1,Obj2)
	print("Check Obj1 if is equal to Obj2: ",Is_Equal)

if __name__ == "__main__":
	main()
