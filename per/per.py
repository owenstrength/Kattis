s = input().lower()
per = "per"
res = 0
for i in range(len(s)):
    if per[i%3] != s[i]:
        res += 1
print(res)