p = int(input())

for _ in range(p):
    k, n = input().split()
    k = int(k)
    n = int(n)
    
    s1 = sum([number for number in range(n+1)])
    s2 = sum([number for number in range(1, 2*n+1, 2)])
    s3 = sum([number for number in range(0, 2*n+1, 2)])

    print(k,s1,s2,s3)