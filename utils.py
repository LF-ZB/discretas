def generate_symbols():
    j = [str(i) for i in range(10)]
    k = [chr(i) for i in range(65,91)]
    l = [chr(i) for i in range(97,123)]
    m = j+k+l
    n = {}
    for i in range(len(m)):
        n[i] = m[i]
    
    return n

def division(a,b):
    return {"b":b,"k":a//b, "r":a%b}

def suma_cuadrados(n):
    return (n*(n+1)*(2*n+1)) / 6

def revertir_cadena(s:str):
    n = len(s) -1
    string_reversed = ""
    for i in range(n+1):
        string_reversed += s[n-i]
    return string_reversed

def divisors(n):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    return d

def mcd(a, b):
    if a < b:
        a,b = b,a
    if a % b == 0:
        return b
    else:
        return mcd(b, b - (a % b))

def mcm(a, b):
    if mcd(a, b) == 1:
        return a*b
    else:
        return int((a*b) // mcd(a, b))
    
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def getMinimunMaddN(mcd1, mcm1):
    mn = mcd1 * mcm1
    d = mcd1**2
    k = mn // d
    c = divisors(k)
    p = []
    r = []

    if len(c) % 2 == 0:
        i = 0
        j = len(c)-1
        while j > i:
            p.append((c[i], c[j]))
            i += 1
            j -= 1
    else:
        i = 0
        j = len(c)-1
        while j >= i:
            p.append((c[i], c[j]))
            i += 1
            j -= 1

    for (x, y) in p:
        a = mcd1*x
        b = mcd1*y
        if mcm(a, b) == mcm1:
            r.append(a+b)
    r.sort()
    return r[0]

        