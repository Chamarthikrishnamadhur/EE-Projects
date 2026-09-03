q=float(input("Enter the value of q: "))
r=int(input("Enter the value of r: "))
sum1=0
for i in range (r+1):
    sum1+=(q**i)
formula =(1/(1-q))-((q**(r+1))/(1-q))
print("Sum is",round(sum1,5))
print("The formula gave",round(formula,5))
if round(sum1,5)==round(formula,5):    
    print("Both are equal")
