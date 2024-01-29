n, m = map(int, input().split())

person1 = sum(list(map(int, input().split())))
print("person1", person1)
scores = []
rankpoints = {1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26, 11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12, 20: 11, 21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1}

for _ in range(m-1):
    scores.append(sum(list(map(int, input().split()))) + 100)
person1 += rankpoints[m]
scores.sort()
scores.reverse()

print(scores)

for i in range(len(scores)):
    if scores[i] < person1:
        print(i+1)
        exit()

print(m)