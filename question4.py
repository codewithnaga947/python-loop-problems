x = int(input("enter any number:"))
y = int(input("enter any number:"))
z = 0
while x <= y:
  if x % 2 == 0:
    print(x)
    z = z + x
  x = x + 1
print(z)
