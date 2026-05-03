# add/cipher.py

def run(n, array):
    # Forcem que siguin enters per si de cas arriba algun residu de text
    try:
        a = int(array[0])
        b = int(array[1])
    except:
        return 0 # Si no es pot convertir, retornem 0 per evitar el crash

    match n:
        case "SCRAMBLE":
            return a ^ b
        case "UNSCRAMBLE":
            return a ^ b
            
    return 0