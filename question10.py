#question no.10
x=int(input("enter any integer:"))
y=0
for i in range(1,x+1):
  if x%i==0:
    y=y+1
if y==2:
  print(x,"is a prime number")    
else:
  print(x,"is not a prime number")
