# В задаче не дано сколько будет учеников. Взял из примера (6 учеников)

students = [[], [], []]

for i in range(6):
    year, surname = input().split()
    if year == '7':
        students[0].append(f'{year} {surname}')
    elif year == '8':
        students[1].append(f'{year} {surname}')
    elif year == '9':
        students[2].append(f'{year} {surname}')

sort = students[0] + students[1] + students[2]
print('\n'.join(sort))
