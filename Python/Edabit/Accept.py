def CheckEven(No):
    return (No % 2 == 0)

def doubles(No):
    return No*2

def sum(A,B):
    return A+B

def filterX(Helper_Function, data):
    result = []
    for no in data:
        if(Helper_Function(no) == True):
            result.append(no)
    return result

def mapX(Helper_Function, data):
    result = []
    for No in data:
        value = Helper_Function(No)
        result.append(value)
    return result

def reduceX(Helper_Function, data):
    ans = 0
    for no in data:
        ans = Helper_Function(ans,no)
    return ans

def main():
    print("Enter number of elements you want enter: ")
    iSize = int(input())

    data_Input = []
    print("Please enter the data")
    for iCnt in range(0, iSize, 1):
        value = int(input())
        data_Input.append(value)

    print("Data is:", data_Input)

    data_filter = filterX(CheckEven, data_Input)
    print("Data after filter is:", data_filter)

    data_map = mapX(doubles, data_filter)
    print("Data after map is:", data_map)

    output = reduceX(sum, data_map)
    print("Data after map is:", output)


if __name__ == "__main__":
    main()
