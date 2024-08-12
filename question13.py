#question no.13
x=int(input("enter a number:"))
y=int(input("enter a number:"))
lcm=0
greater=x if x>y else y
while True:
  if greater%x==0 and greater%y==0:
    lcm=greater
    break
  greater+=1
print("lcm of given two numbers=",lcm)
