#question no.09
x=int(input("enter any integer:"))
y=0
for i in range(1,x):
  if x%i==0:
    print(i)
    y+=i
    
if y==x:
  print("it is a perfect number")
else:
  print("it is not a perfect number")
