a = int(input("enter first number"))
b = int(input("enter second number"))
n = int(input("how many digits want to you print "))
print(a)
print(b)
while ( n > 0 ):
    n = n-1
    temp = a + b
    a = b
    b = temp
    print(temp)


