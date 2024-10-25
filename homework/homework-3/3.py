line = input()
words = []

while line != '':
    for word in line.split():
        print(words.count(word), end=' ')
        words.append(word)
    line = input()

