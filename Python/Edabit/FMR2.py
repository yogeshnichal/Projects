
def main():
    print("Enter number of elements you want enter: ")
    iSize = int(input())

    data_Input = []
    print("Please enter the data")
    for iCnt in range(0, iSize, 1):
        value = int(input())
        data_Input.append(value)

    print("Data is:", data_Input)


if __name__ == "__main__":
    main()
