# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/vote

def main(Arr):
    total = 0
    votes = []
    for i in Arr:
        total += i
        votes.append(i)
    
    unqiue = [item for item in Arr if Arr.count(item) == 1]

    if len(set(Arr)) == 1 or len(unqiue) == 0:
        print("no winner")
        return

    max_vote = 0
    possible_tie = False
    for i in range(len(votes)):
        if votes[i] > total/2:
            print("majority winner", i+1)
            return
        else:
            if votes[i] > max_vote:
                max_vote = votes[i]
                max_index = i
    
    print("minority winner", max_index+1)

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        Arr = []
        for _ in range(n):
            Arr.append(int(input()))
        main(Arr)
