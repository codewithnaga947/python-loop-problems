#question no.14
x=int(input("enter any number:"))
y=int(input("enter any number:"))
smaller=x if x<y else y
i=1
hcf=0
while i<=smaller:
  if x%i==0 and y%i==0:
    hcf=i
  i=i+1
print(hcf)
