from itertools import combinations
from pip._vendor.distlib.compat import raw_input

string, value = raw_input().split()

for i in range(1, int(value) + 1):
    for j in combinations(sorted(string), i):
        print("".join(j))