s = input()

stack = []

for c in s:
    if c == "<":
        stack.pop()
    else:
        stack.append(c)

print("".join(stack))
