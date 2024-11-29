num=int(input("Enter the number : "))
a=0
b=1
print("The Fibonacci Series :")
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
