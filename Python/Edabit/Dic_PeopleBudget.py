# # Get Sum of People's Budget

def main():
    ky = []
    size = int(input("Enter size of dic: "))

    for i in range(size):
        ky = [
                {"Name": input("name:"), "Age": input("age:"), "Budg": input("budg:")},
                {"Name": input("name:"), "Age": input("age:"), "Budg": input("budg:")}
        ]
    my_data = ky
    print(my_data)


if __name__ == "__main__":
    main()