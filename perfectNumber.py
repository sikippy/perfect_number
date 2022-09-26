import math
number = input("enter a number :");
i = 10**math.ceil(len(number)/2)

#check if the number is a perfect number or not
number = int(number)
if(number<i):
    i= number
sumOfNumber =[1]
for x in range (2, i ):
   if(number/x-math.floor(number/x)==0):
        sumOfNumber.append(x)
        sumOfNumber.append(number/x)
        
print(sumOfNumber)
sumOfNumber = list(dict.fromkeys(sumOfNumber))
print(sum(sumOfNumber))
if sum(sumOfNumber) ==number:
    print("yes, it is perfect")
