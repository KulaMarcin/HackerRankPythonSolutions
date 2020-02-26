a = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, quantity_of_elements = input().split()
    elements = map(int, input().split())
    if operation == "intersection_update":
        A.intersection_update(set(elements))
    elif operation == "update":
        A.update(set(elements))
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(set(elements))
    elif operation == "difference_update":
        A.difference_update(set(elements))

print(sum(A))

