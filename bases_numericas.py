import utils

SYMBOLS = utils.generate_symbols()

def convertir_base(n:int,b:int) -> str:
    n_base_b = ""

    while True:
        div = utils.division(n,b)
        n_base_b += str(div["r"])
        n = div["k"]
        if n < b:
            n_base_b += SYMBOLS[n]
            break
    return n_base_b


def revertir_base(n_base_b:str, b:int) -> int:
    n_reverse = 0
    n = len(n_base_b)
    for i in range(n):
        m = int(n_base_b[i])
        n_reverse += m*b**i
    return n_reverse

def sum(*args, base=2):
    total = 0
    for i in args:
        total += revertir_base(i, base)
    return total



def main():
    x = convertir_base(20,2)

    y = "10100"

    print(revertir_base(x, 2))
    
    x = utils.revertir_cadena(x)
    if x == y:
        print(x)
    else:
        raise Exception(f"Respuesta: {y} \n Tu Resultado: {x}")
if __name__ == "__main__":
    main()