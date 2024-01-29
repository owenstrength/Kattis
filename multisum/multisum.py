def find_sum_range(arr, target):
    arr.sort()
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    best_start, best_end = None, None
    best_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            cur_sum = prefix_sum[j + 1] - prefix_sum[i]
            if cur_sum == target:
                return (i, j)
            elif cur_sum < target and cur_sum > best_sum:
                best_start, best_end = i, j
                best_sum = cur_sum
    if best_start is not None:
        return (best_start, best_end)
    else:
        return None

arr = [1,3,5,4,8,13]
tar = 7
res = find_sum_range(arr,tar)
print(res)
print(sum(arr[res[0]:res[1]+1]))