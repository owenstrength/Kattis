n = int(input())
l = input()

hashparen = {'(':')','[':']', '{':'}'}
opens = ['(','{','[']
closes =[')','}',']']
stack = []

for i, char in enumerate(l):
    if char in opens:
        stack.append(char)
    elif char in closes:
        if len(stack) != 0:
            item = stack[-1]
        else:
            print(char, i)
            break
        if char != hashparen[item]:
            print(char, i)
            break
        else:
            stack.pop()
else:
    print('ok so far')
