#question no.12
x=int(input("enter any integer:"))
for i in range(1,x+1):
  if i*i*i==x:
    x="perfect_cube"

if x=="perfect_cube":
  print("it is a perfect cube number")    
else:
  print("it is not a perfect cube number")
