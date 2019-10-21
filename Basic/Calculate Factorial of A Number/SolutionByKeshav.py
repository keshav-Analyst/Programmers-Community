#Factorial
#input the digit for which the factorial is to be calculated 
n= int(input())
#create a temp variable
fact=1
for i in range(1,n+1):
    fact=fact*i
    
#print the result
print(fact)
    
