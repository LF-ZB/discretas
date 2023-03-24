import utils
def ecuaciones_diofanticas(a,b,r):
    if r % utils.mcd(a,b) != 0 :
        raise Exception("esta ecuacion no tiene solucion")
    return True
    

