n = int(input())
import math
def secretmessage(s):
    length = len(s)
    m = math.ceil(length ** 0.5)
    l = m ** 2
    s += "*" * (l-length)
    grid = []
    res = ""
    for _ in range(m):
        grid.append([])

    resGrid = []
    
    for i in range(m):
        for j in range(m):
            item = s[j + (m*i)]
            grid[i].append(item)

    for i in range(m):
        temp = []
        for j in range(m):
            x = m-j - 1
            temp.append(grid[x][i])
        resGrid.append(temp)
    for i in range(m):
        for j in range(m):
            item = resGrid[i][j]
            if item != "*":
                res += item
    print(res)

for _ in range(n):
    secretmessage(input())