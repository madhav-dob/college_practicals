name = input("Enter the name:")

for i in name:
    if i.isalpha():
        pass
    else:
        raise Exception("The name entered contains digits or special characters")



