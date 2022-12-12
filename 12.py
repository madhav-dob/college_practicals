import  math

l = list(input('Enter the list :'))
l2 = []
for i in l :
    if i.isnumeric():
        t =int(i) % 2
        print(t)
        if t == 0:
            l2.append(math.pow(i,3))


print(l2)