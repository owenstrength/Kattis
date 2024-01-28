n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    for i in range(2,len(nums)):
        if nums[i] != nums[i-1] + 1:
            print(i)
            break