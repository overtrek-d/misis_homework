text = input()

word = dict()

while text != '':
    for i in text.split():
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    text = input()

sort = dict()
for key, value in word.items():
    if value not in sort:
        sort[value] = [key]
    else:
        sort[value].append(key)

for i in range(max(sort.keys()), min(sort.keys()) - 1, -1):
    if i in sort:
        line = sort[i]
        print('\n'.join(sorted(line)))