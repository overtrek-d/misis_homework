# Возможно не понял суть задания.

seq = input()
stack = []

for i in seq:
    if i not in '()[]':
        pass
    elif i in '[(':
        stack.append(i)
    elif i in ')]' and len(stack) == 0:
        print('No')
        exit()
    elif i in '])' and (i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '['):
        stack.pop()
    else:
        print('No')
        exit()

if len(stack) == 0:
    print('Yes')
else:
    print('No')
