# range (start, end, displacement)
# start: is by default _____
# end: There is no default value
# displacement is by default 1

for i in range(1,5):
    print(i)

print("_____________________________")

for i in range(0, 10, 2):
    print(i)

print("_____________________________")

value = [10, 20, 30, 40, 50]
for i in range(0, len(value), 1):      # last 1 can remove # displacement
    print(value[i])

print("_____________________________")