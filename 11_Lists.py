N = int(input())
created_list = []

for _ in range(N):
    operation, *parameters = input().split()
    values = list(map(int, parameters))
    if operation == "print":
        print(created_list)
    elif operation == "insert":
        created_list.insert(values[0], values[1])
    elif operation == "pop":
        created_list.pop()
    elif operation == "append":
        created_list.append(values[0])
    elif operation == "reverse":
        created_list.reverse()
    elif operation == "sort":
        created_list.sort()
    elif operation == "remove":
        created_list.remove(values[0])


