def is_diabolic(n):
    "666" in str(n):

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n-1):
        if (n%i)==0:    
            return False
    return True

d=0

for i in range(100000):
    if is_prime(i)==True:
        if is_diabolic(i)==True:
            print(n)
            d+=1
print (d)



