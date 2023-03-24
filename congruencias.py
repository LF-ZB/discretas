import utils


def verificar_conguencia(a,b,n):
    return (a-b % n == 0)

def hallar_inverso(a,n):
    if utils.mcd(a,n) != 1:
        raise Exception("No es posible encontrar el inverso")
    r = 1
    i = 1
    j = a * i
    while True:
        if j > n:
            j = j % n
            r *= i
            i = 1
            if r > n:
                r = r % n
            
            if j % n == 1:
                return r
        i +=1


def main():
    pass
if __name__ == "__main__":
    main()

#############################################
#   Propiedades de congruencias             #
#############################################
#                                           #
#   a≡a mod n                               #
#   a≡b mod n → b≡a mod n                   #
#   a≡b mod n || b≡c mod n → a≡c mod n      #
#   a≡b mod n || c≡d mod n → a+d≡c+b mod n  #
#   a≡b mod n || b≡c mod n → ac≡bd mod n    #
#   a≡b mod n → a^k ≡ b^k mod n             #
#                                           #
#############################################
