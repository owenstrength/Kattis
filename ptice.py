n = int(input())
s = input().upper()

adrian = "ABC"
adrian_score = 0
brunno = "BABC"
brunno_score = 0
goran = "CCAABB"
goran_score = 0

for i in range(len(s)):
    if s[i] == adrian[i%3]:
        adrian_score += 1

    if s[i] == brunno[i%4]:
        brunno_score += 1

    if s[i] == goran[i%6]:
        goran_score += 1

largest = (max(adrian_score, brunno_score, goran_score))
print(largest)
if largest == adrian_score:
    print("Adrian")

if largest == brunno_score:
    print("Bruno")

if largest == goran_score:
    print("Goran")