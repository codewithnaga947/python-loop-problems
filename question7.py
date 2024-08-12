#question no.7
x = int(input("enter any number:"))
i = 1
j=0
while i<=x:
  if x%i==0:
    print(i)
    j+=i
  i=i+1  
print("sum=",j)
