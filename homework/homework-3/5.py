line = input()
num, sym = 0, 0
l_sym = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in line:
    if char == '.':
        break
    elif char.lower() in l_sym:
        sym += 1
    elif char in nums:
        num += 1

print(num, sym)