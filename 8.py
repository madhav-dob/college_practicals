a = input('Enter :')
dic = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE',}
if a.isalpha():
    print("Given character is an alphabet")
    if a.isupper():
        print("and it is in upper case")
    else:
        print("and it is in lower case")
elif a.isalnum():
    print("Given character is a number")
    print(dic[int(a)])

else:
    print("Given character is a special character")



