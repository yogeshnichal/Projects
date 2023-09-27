def main():
    fruit = list()

    size = int(input("Enter how many elements you want to store: "))

    print("Please enter the values: ")

    for i in range(0, size):
        add = int(input())
        fruit.append(add)      # fruit.insert(i, add)

    print(fruit)


if __name__ == "__main__":
    main()