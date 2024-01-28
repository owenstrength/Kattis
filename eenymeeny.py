message = input().split()
m = len(message) - 1
n = int(input())
people = []
for _ in range(n):
    people.append(input())

t = 0
team1 = []
team2 = []
team = 1

while len(people) > 0:
    t = (t+m) % len(people)
    if team == 1:
        team1.append(people.pop(t))
        team = 2
    else:
        team2.append(people.pop(t))
        team = 1

print(len(team1))
for member in team1:
    print(member)

print(len(team2))
for member in team2:
    print(member)