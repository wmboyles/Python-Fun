def add(m, a):
    out = ""
    for i in range(len(m)):
        if m[i] == a[i]: out += "0"
        else: out += "1"
    return out


def main():
    N1 = '0110100110010110'  # Rotational and mirror symmetry
    
    N2 = '1001111111111001'  # 2-way rotational symmetry
    N3 = '1111011001101111' 

    N4 = '1110010100110001'  # 4-way rotational symmetry
    N5 = '1000110010100111'
    N6 = '0001001101011110'
    N7 = '0111101011001000'

    N8 = '0011010011010101'  # 4-way rotational & 4-way mirror symmetry
    N9 = '1100001010111010'
    N10 = '0101110101000011'
    N11 = '1010101100101100'
    N12 = '1101000111100100'
    N13 = '0100111000011101'
    N14 = '1011100001110010'
    N15 = '0010011110001011'

    Nulls = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15]

    boards = []
    for i in range(2 ** 16): boards.append(("{0:b}".format(i)).zfill(16))

    totalSums = []
    for b in boards:
        sums = []
        for n in Nulls: sums.append(add(b, n).count("1"))
        totalSums.append(min(sums))
    print(max(totalSums))
        
