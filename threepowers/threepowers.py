n = int(input())

while(n != 0):
    res = []
    bin_n = bin(n-1)

    bin_n = bin_n[2:][::-1]
    
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            res.append(str(3 ** (i)))

    format = ", ".join(res)
    format = "{ " + format + " }"
    print(format)

    n = int(input())
