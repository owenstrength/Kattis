n = int(input())
s = input()

# find largest number in s
largest = 0
for i in range(n):
    for j in range(i, n):
        if not s[j].isdigit():
            break
        if int(s[i:j+1]) > largest:
            largest = int(s[i:j+1])
print(largest)
