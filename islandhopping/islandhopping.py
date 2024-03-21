from collections import defaultdict
from heapq import heappush, heappop, heapify
from functools import lru_cache

n = int(input())

@lru_cache
def solve(m, edges):
    edges = eval(edges)
    def dist(a, b):
        return (abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2) ** 0.5
    
    def generate_weights(m, edges):
        edges_dict = defaultdict(list)
        for i in range(m):
            for j in range(i+1, m):
                edges_dict[i].append((j, dist(edges[i], edges[j])))
                edges_dict[j].append((i, dist(edges[i], edges[j])))
        return edges_dict
    
    def prims(m, edges):
        edges = generate_weights(m, edges)
        curr_edges = curr_edges = [
            (cost, 0, dest)
            for dest, cost in edges[0]
            ]

        heapify(curr_edges)
        mst = set()
        visited = {0}
        total_weight = 0
        start = 0
        visited.add(start)
        while curr_edges and len(visited) < m:
            cost, src, dest = heappop(curr_edges)
            if dest not in visited:
                visited.add(dest)
                mst.add((src, dest, cost))
                total_weight += cost
                for c_dest, c_cost in edges.get(dest, []):
                    if c_dest not in visited:
                        heappush(curr_edges, (c_cost, dest, c_dest))
        return total_weight

    
    return prims(m, edges)

for _ in range(n):
    m = int(input())
    edges = [list(map(float, input().split())) for _ in range(m)]
    edges = str(edges)
    print(solve(m, edges))