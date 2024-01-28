m, n = map(int, input().split())


def in_bounds(x, y): return 0 <= x < m and 0 <= y < n


neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

grid = []
cnt = 0
end = (m-1,n-1)
print("end", end)
for _ in range(m):
    grid.append(list(input()))


def dfs(x,y, path):
    if (x,y) == end:
        print("Found Path")
        print(path)
        return True
        exit()
    for dx, dy in neighbors:
        new_x = x + dx* int(grid[x][y])
        new_y = y + dy* int(grid[x][y])
        print("Path", path)
        if in_bounds(new_x, new_y) and int(grid[new_x][new_y]) != 0 and (new_x, new_y) not in path:
            if dfs(new_x, new_y, path + [(new_x, new_y)]):
                print(path)
                return
    return -1

print(dfs(0,0,[(0,0)]))