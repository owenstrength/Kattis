c, x, m = map(float, input().split())

res = 0
for _ in range(6):
    speed, mpg = input().split()
    speed = int(speed)
    mpg = float(mpg)
    costPerHour = x+speed/mpg
    hours = m/speed
    
    if (costPerHour*hours <= c/2.0):
        res = max(res, speed)

if res != 0:
    print("YES", res)
else:
    print("NO")