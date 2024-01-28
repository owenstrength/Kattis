option, s = input().split()
out = ""
prev = ""
count = 0
if option == "E":
    for letter in s:
        if letter != prev:
            out += prev
            out += str(count)
            count = 1
            prev = letter
        else:
            count += 1
    out += prev
    out += str(count)
    print(out[1:])
else:
    i = 0
    while i < len(s):
        letter = s[i]
        count = int(s[i + 1])
        for j in range(count):
            out += letter
        i += 2
    print(out)