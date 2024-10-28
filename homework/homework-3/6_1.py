#Реально без min и max
n = int(input())
line = input().split()
nums = []
min, max = int(line[0]), int(line[1])
for i in line:
    if int(i) < min:
        min = int(i)
    if int(i) > max:
        max = int(i)
    nums.append(int(i))

for i in range(n):
    if nums[i] == min:
        nums[i] = max
    elif nums[i] == max:
        nums[i] = min

print(' '.join(map(str, nums)))