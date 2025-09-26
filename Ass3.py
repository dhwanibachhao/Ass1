#Task 1
num=int(input("Enter a number :"))
def factorial(num1):
    fact=1
    if num<2:
        print ("factorial is 1")
    else :
        #factorial = num* (fact(num-1))
        
        for i in range(1,num1+1):
            fact*=i
        return fact
        
print("Factorial of ",num, "is :" ,factorial(num))

#Task 2
import math
num=float(input("Enter a number :"))

square_root=math.sqrt(num)
natural_log=math.log(num)
sine_of_num=math.sin(num)

print("Results:")
print("Square root of ",num,"is :",square_root)
print("Natural log of ",num,"is",natural_log)
print("Sine of ",num,"is",sine_of_num)

