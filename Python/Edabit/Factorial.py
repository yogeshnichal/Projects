# factorial 5 = 5*4*3*2*1 =120

num = int(input ('Enter the number:'))
fact = 1
while num > 1:
    fact = fact * num
    num = num -1

print ('Factorial is:', fact)
