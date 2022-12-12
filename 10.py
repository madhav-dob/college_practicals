str1 = input('Enter the string 1 :')
str2 = input('Enter the string 2 :')


n  = int(input("Enter the number n :"))
mm = str1[0:n]
nn = str2[0:n]
MM = str1[n:]
NN = str2[n:]

str1 = mm+ NN
str2 = nn + MM



print(str1)
print(str2)