import collections

number_of_shoes = int(input().strip())
shoes = collections.Counter(map(int, input().split()))
number_of_customers = int(input().strip())

revenue = 0

for i in range(number_of_customers):
    size, price = map(int, input().split())
    if shoes[size]:
        revenue += price
        shoes[size] -= 1

print(revenue)



