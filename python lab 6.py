#count no of odd and even

n=int(input("Enter the Number :"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the Elements : ")))
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"No.of Odd numbers : {even}")
print(f"No.of Even numbers : {odd}")
