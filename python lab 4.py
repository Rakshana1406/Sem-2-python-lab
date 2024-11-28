num=int(input("Enter the number : "))
a=0
b=1
next_num=b
count=1

while count <= num:
    print(next_num,end = "  ")
    count +=1
    a,b=b,next_num
    next_num=a+b
print()    
