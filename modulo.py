nums = []

for _ in range(10):
    nums.append(int(input()))

mod_nums = []
for num in nums:
    mod_nums.append(num % 42)

print(len(set(mod_nums)))