def div(a,b):
    i = 0
    while len(b) <= len(a[i:]):
        if int(a[i]) == 1:
            for j in range(len(b)):
                a[i+j] = abs(int(a[i+j]) - int(b[j]))
        i += 1
    return(a)

def crc_32(line):
    g = list('100000' + bin(int('04C11DB7', 16))[2:])
    bin_line = list(''.join(bin(ord(x))[2:] for x in line)+'0'*(len(g)-1))
    string = div(bin_line, g)[-32:]
    arr = ''.join(list(map(str, string)))
    return hex(int(arr, 2))[2:]
    
if __name__ == '__main__':
    line = input('input: ') # test
    print('hash', crc_32(line)) # 749d77bb
