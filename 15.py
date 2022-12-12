import math
def dict_maker():
    dic = {}
    for i in range(1,6):
        dic[i] = int(math.pow(i,3))

    print(dic)

dict_maker()