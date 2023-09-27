d = {}

size = int(input("Enter the size of nested dictionary: "))

for i in range(size):
    dict_name = input("Enter the name of child dictionary: ")

    d[dict_name] = {}
    Name = input("Enter name: ")
    Age = input("Enter Age: ")
    d[dict_name]["Name"] = Name
    d[dict_name]["Age"] = Age

print(d)