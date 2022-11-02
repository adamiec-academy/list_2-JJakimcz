def is_diabolic(n):
    if "666" in str(n):
        print(n)
        return True
    else:
        return False

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n-1):
            if (n%i)==0:    
                return False
            else:
                return True
d=0

for i in range(100000):
    if is_prime(i)==True:  
        if is_diabolic(i)==True:
            d+=1
print (d)



