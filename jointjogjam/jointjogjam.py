points = list(map(int, input().split()))

a_start = (points[0], points[1])
b_start = (points[2], points[3])
a_end = (points[4], points[5])
b_end = (points[6], points[7])

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

start_dist = dist(a_start, b_start)
end_dist = dist(a_end, b_end)

print(max(start_dist, end_dist))