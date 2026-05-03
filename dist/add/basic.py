def SUM(A, B): 
    return A + B 

def SUB(A, B):
    return A - B

def MULT(A, B):
    return A * B

def DIV(A, B):
    try:
        return A / B
    except ZeroDivisionError:
        return 0

def XOR(A, B):
    return A ^ B

def SHIFT(A, B):
    if not A:
        return A
    B = B % len(A)
    return A[B:] + A[:B]

def ROT(A, B):
    res = ""
    for c in A:
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            res += chr((ord(c) - start + B) % 26 + start)
        else:
            res += c
    return res

def REV(A):
    return A[::-1]


def run(n, array):
    args = [int(i) for i in array]
    a = args[0]
    b = args[1]
    
    match n:
        case "SUM":
            result = SUM(a, b)
        case "SUB":
            result = SUB(a, b)
        case "MULT":
            result = MULT(a, b)
        case "DIV":
            result = DIV(a, b)
        case "XOR":
            result = XOR(a, b)
        case "SHIFT":
            result = SHIFT(a, b)
        case "ROT":
            result = ROT(a, b)
        case "REV":
            result = REV(a)
 
    return result