d = set()
words = int(input())
prev = input()
d.add(prev)
count = 1
while count < words:
    next = input()
    if prev[-1] == next[0] and next not in d:
        d.add(next)
        prev = next
        count += 1
    else:
        if count % 2 == 1:
            print("Player 2 lost")
        else:
            print("Player 1 lost")

        break
else:
    print("Fair Game")