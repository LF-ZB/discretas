
def residuos_de_potencias(numero, exponente, divisor):
    residuos = []
    for e in range(1,divisor):
        r = (numero ** e) % divisor
        if r == 1:
            residuos.append({"r":r, "e":e})
            break
        else:
            residuos.append({"r":r, "e":e})
        

    residuo_modular = residuos[exponente % residuos[len(residuos)-1]["exponente"] - 1]

    return residuo_modular

def ultimo_digito(base, exponente):
    base = base % 10
    rs = []
    for i in range(1,exponente+1):
        r = base**i % 10
        rs.append({"r":r, "e":i})
        if r == 1:
            break
    n = exponente % rs[len(rs)-1]["e"]

    return rs[n-(n==0)]["r"]



def main():
    pass
if __name__ == "__main__":
    main()