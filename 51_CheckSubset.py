

for _ in range(int(input())):
    a_size, a, b_size, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))