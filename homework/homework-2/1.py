l, r = (int(i) for i in input().split())
i = 0
while 2**i <= r:
    if 2**i >= l:
        print(2**i)
    i += 1