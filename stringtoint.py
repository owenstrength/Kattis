def myAtoi(self, s: str) -> int:
    s = s.lstrip()
    isNegative = False
    if "-" in s:
        isNegative = True
        s = s[1:]
    elif "+" in s:
        s = s[1:]
    leadingZeroes = True
    num_s = ""
    for c in s:
        if not c.isnumeric():
            break
        if c != "0" and c.isnumeric() or c == "0" and not leadingZeroes:
            leadingZeroes = False
            num_s += c

    return int(num_s) if not isNegative else -int(num_s)
