n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command, *value = input().split()
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(value[0]))
    elif command == "discard":
        s.discard(int(value[0]))

print(sum(s))

