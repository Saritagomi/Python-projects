elements_num = int(input())
elements = set(map(int, input().split()))
commands_num = int(input())
for _ in range(commands_num):
    command = input().split(" ")
    if command[0] == 'pop':
        elements.pop()
    elif command[0] == 'remove':
        elements.remove(int(int(command[1])))
    elif command[0] == 'discard':
        elements.discard(int(int(command[1])))

print(sum(elements))
