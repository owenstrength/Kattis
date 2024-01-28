# jackpot periodicity calculation
n = int(input())
while n != 0:
    w = int(input())
    if w > 1:
        vals = [map(int, input().split())]
    else:
        vals = [int(input())]

    # return smallest common multiple of all numbers in vals
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(vals):
        if len(vals) == 1:
            return vals[0]
        else:
            return lcm([vals[0] * vals[1] // gcd(vals[0], vals[1])] + vals[2:])

    print(lcm(vals))
    n -= 1
