print("Example of boolean data types")
def exp(value):
    ans = bool(value <=0)
    return ans

def main():
    print("Enter a first number: ")
    num1 = int(input())

    out = exp(num1)
    print("Is less then equals to zero is: ",out)

if __name__ == "__main__":
    main()


