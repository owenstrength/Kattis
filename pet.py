list1 = sum(map(int, input().split()))
list2 = sum(map(int, input().split()))
list3 = sum(map(int, input().split()))
list4 = sum(map(int, input().split()))
list5 = sum(map(int, input().split()))

winner = 0
winner_total = 0
if list1 > winner_total:
    winner_total = list1
    winner = 1
if list2 > winner_total:
    winner_total = list2
    winner = 2
if list3 > winner_total:
    winner_total = list3
    winner = 3
if list4 > winner_total:
    winner_total = list4
    winner = 4
if list5 > winner_total:
    winner_total = list5
    winner = 5
print(winner, winner_total)
