n = input()

if int(n) < 148:
    print("99")
    exit()

testn = list(n)
testn[-1] = "9"
testn[-2] = "9"

testn = "".join(testn)

if int(testn) - int(n) <= 50:
    print(testn)
else:
    print(int(testn) - 100)