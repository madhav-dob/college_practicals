a = int(input("Length of Pyramid: "))
b = " "
c = "* "
y = 0
x = a
for i in range(a):
  print(x*b,y*c)
  y += 1
  x -= 1
z = 0
for i in range(a):
  print(z*b,a*c)
  a -= 1
  z += 1