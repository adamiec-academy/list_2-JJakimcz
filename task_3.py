n=100000

def is_diabolic(n):
    x=0
    sigma=str(n)[:-3]
    if sigma=="666":
        x = x + 1
        print ("liczba diabelska: ",n)
        print ("która: ",x)
        return True
    else:
        print("liczba nie diabelska: ",n)
        return False

def is_prime(n):
    for n in range(2,100000):
        for i in range(2,n-1):
            if (n%i)==0:    
                print("liczba nie pierwsza przy dzieleniu: ",n)
                print("przez: ",i)
            else:
                break
            print("liczba pierwsza nie",n)
            is_diabolic(n) 


is_prime(n)



