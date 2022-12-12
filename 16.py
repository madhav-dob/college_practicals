t1 = (1,2,5,7,9,2,4,6,8,10)

# section 1
length = int(len(t1)/2)

print(t1[:length])
print(t1[length:])

# section2
new_list = []
for i in t1:
    if i%2 == 0:
        new_list.append(i)
print(new_list)


# section 3
t2 = (11,13,15)
t3 = t1 + t2
print("Tuple after joining two is:, t3")

#section 4

print("Maximum value:", max(t1))
print("Minimum value:", min(t1))
