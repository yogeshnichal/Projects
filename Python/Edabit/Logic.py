print("Area of Triangle")

def Triangle(value1, value2, value3):
    ans = (value1 * value2) / value3
    return ans

def main():
    print("Triangle base is: ")
    base = float(input())
    print("Triangle Height is: ")
    height = float(input())
    print("Divided by 2: ")
    div_value = int(input())

    formula = Triangle(base,height,div_value)
    print("The area of triangle is: ",formula)

if __name__ == "__main__":
    main()