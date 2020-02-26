from pip._vendor.distlib.compat import raw_input

N = int(input())
set1 = set(map(int, raw_input().split()))

M = int(input())
set2 = set(map(int, raw_input().split()))

symmetric_differences = (set1.difference(set2)).union(set2.difference(set1))

for i in sorted(list(symmetric_differences)):
    print(i)
