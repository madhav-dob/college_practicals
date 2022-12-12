import math

n = int(input("Enter the number : "))

def check_prime(n):
    con =0
    for i in range(2,int(math.sqrt(n))+1):
        if n %i == 0:
            con = 1

        else:
            pass
    if con == 1:
        return False
    else:
        return True


def find_prime_num(n):
    l = []
    for i in range(1,n):
        con = check_prime(i)
        if con == True:
            l.append(i)
    print(l)

def find_n_primes(n):
    l =[]
    k = 1
    while len(l) < (n):
        con = check_prime(k)
        if con == True:
            l.append(k)
        k += 1
    print(l)

print(check_prime(n))
find_prime_num(n)
find_n_primes(n)