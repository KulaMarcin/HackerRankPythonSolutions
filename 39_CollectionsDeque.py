from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    command, *value = input().split()
    if command == "append":
        d.append(int(value[0]))
    elif command == "appendleft":
        d.appendleft(int(value[0]))
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()


output = " ".join(str(i) for i in d)
print(output)