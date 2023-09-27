# Long = 92
# Wide = 48.8
# area = Long * Wide
# print("area is:", area )
#
# Packets = 9
# Costs = 1.49
# Dollar = 20
# Return = (Dollar-Packets*Costs)
# print(Return)
#
# length = 5.5
# costs = 500
# area = length**2
# print("Bathroom tiles total costs:",area*costs)
#
# num = 20
# print("binary of number 17 is:", format(num,'b'))
#
# street = "Ring road"
# city = "Nanded"
# country = "India"
# print(street+' '+city+' '+country)

# Fruits = 5
# Vegetables = 3
# x = Fruits
# y = Vegetables
# print(f"I eat fruits {x} {y}.")

# S = "Maine 200 banana khaye."
# S = S.replace ("200", "10").replace("banana", "samosa")
# print(S)

# s='Earth revolves around the sun'
# print(s[0:14])
# print(s[-7:])

exp = [2200, 2350, 2600, 2130, 2190]
refund = 200
print("Jan extra compare to Feb:",exp[1]-exp[0],'\n' "First three months:", exp[0]+exp[1]+exp[2], '\n' "2000 exactly spent any month:", 2000 in exp)
exp.append(1980)
print("Exp list end of June:",exp)
exp[3] = exp[3] - 200
print("after got 200 refund in Apr:",exp)
