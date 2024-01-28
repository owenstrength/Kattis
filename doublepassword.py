a = input()
b = input()

cnt = 4
for i in range(4):
    if a[i] == b[i]:
        cnt -= 1

print(2 ** cnt)
