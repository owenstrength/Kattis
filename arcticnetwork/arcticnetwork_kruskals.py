n = int(input())

def solve(s, p, edges):
    def dist(a, b):
        return (abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2) ** 0.5
    
    parents = [i for i in range(p+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    def generate_weights(p, edges):
        weights = []
        for i in range(p):
            for j in range(i+1, p):
                weights.append((i, j, dist(edges[i], edges[j])))
        return weights

    def kruskal(s, p, edges):
        weights = generate_weights(p, edges)
        mst = set()
        # take the edges in sorted order (min weight first)
        for src, dest, weight in sorted(weights, key=lambda x: x[2]):
            if find(src) != find(dest):
                union(src, dest)
                mst.add((src, dest, weight))

        # sort the mst by weight
        mst = sorted(mst, key=lambda x: x[2])
        for i in range(s-1):
            mst.pop()
        
        return mst[-1][2]
    
    return kruskal(s, p, edges)

for _ in range(n):
    s, p = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(p)]
    print(f"{solve(s, p, edges):.2f}")