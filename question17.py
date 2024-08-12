x = str(int(input("enter any number:")))
y=len(x)
while True:
  print(x[y-1],end=" ")
  y=y-1
  if y==0:
    break
