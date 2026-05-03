def HASH_FNV(data):
    h = 2166136261
    for char in str(data):
        h ^= ord(char)
        h = (h * 16777619) & 0xFFFFFFFF
    return h

def VIGENERE(data, key, mode):
    d_str = str(data)
    k_str = str(key)
    while len(d_str) % 3 != 0: d_str = "0" + d_str
    while len(k_str) % 3 != 0: k_str = "0" + k_str
    
    d_blocks = [int(d_str[i:i+3]) for i in range(0, len(d_str), 3)]
    k_blocks = [int(k_str[i:i+3]) for i in range(0, len(k_str), 3)]
    
    res = ""
    for i in range(len(d_blocks)):
        k_val = k_blocks[i % len(k_blocks)]
        if mode == 1:
            new_val = (d_blocks[i] + k_val) % 256
        else:
            new_val = (d_blocks[i] - k_val) % 256
        res += f"{new_val:03d}"
    return int(res)

def MODEXP(base, exp, mod):
    return pow(base, exp, mod)

def run(n, array):
    args = [int(i) for i in array]

    a = args[0]
    b = args[1]
    
    match n:

        case "HASH":
            return HASH_FNV(a)
        case "VIG_ENC":
            return VIGENERE(a, b, 1)
        case "VIG_DEC":
            return VIGENERE(a, b, -1)
        case "POWER":
            return MODEXP(a, b, args[2] if len(args) > 2 else 0xFFFFFFFF)