print("Multiplication Exercise")

def multiplication(value1, value2):
    Ans = value1 * value2
    return Ans

def multi():
    print("Enter first value: ")
    No1 = float(input())
    print("Enter second value: ")
    No2 = float(input())

    m = multiplication(No1,No2)
    print("Multiplication value is", m)

if __name__ == "__main__":
    multi()