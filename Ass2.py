#Task 1: Even Or Odd Number
a=int(input("Enter an integer: "))
if(a%2==0):
    print(a,"This is Even number.")
else:
    print(a,"This is Odd number.")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1,51):
    print(i)
    sum=sum+i
print(sum)