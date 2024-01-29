word = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for char in word:
    if char == "_":
        whitespace += 1
    elif char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    else:
        symbols += 1

print(whitespace / len(word))
print(lowercase / len(word))
print(uppercase / len(word))
print(symbols / len(word))
