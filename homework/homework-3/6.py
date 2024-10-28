#Сделал так тк .index() выдавал ошибку
n = int(input())
nums = []
for i in input().split():
    nums.append(int(i))

min_num, max_num = sorted(nums)[0], sorted(nums)[-1]# Без min() и max() :3

for i in range(n):
    if nums[i] == min_num:
        nums[i] = max_num
    elif nums[i] == max_num:
        nums[i] = min_num
print(' '.join(map(str, nums)))