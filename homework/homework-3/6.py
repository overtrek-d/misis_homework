#Сделал так тк .index() выдавал ошибку
n = int(input())
nums = []
for i in input().split():
    nums.append(int(i))

min_num, max_num = min(nums), max(nums)

for i in range(n):
    if nums[i] == min_num:
        nums[i] = max_num
    elif nums[i] == max_num:
        nums[i] = min_num
print(' '.join(map(str, nums)))