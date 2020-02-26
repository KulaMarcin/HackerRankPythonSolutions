from itertools import combinations_with_replacement

string, value = input().split()

for i in combinations_with_replacement(sorted(string), int(value)):
    print("".join(i))