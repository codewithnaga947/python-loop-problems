#question no.11
x=int(input("enter any integer:"))
for i in range(1,x+1):
  if i*i==x:
    x="perfect"

if x=="perfect":
  print("it is a perfect square number")    
else:
  print("it is not a perfect square number")
