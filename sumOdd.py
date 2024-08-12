x=int(input("enter any integer:"))
y=int(input("enter another integer:"))
sum=0
while x<=y:
  if x%2!=0:
    print(x)
    sum+=x
  x=x+1 
print("-------------")  
print("sum=",sum)
