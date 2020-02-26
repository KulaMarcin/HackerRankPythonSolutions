from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
arr = map(int, raw_input().split())
arr = list(arr)
maximum = max(arr)

for x in range(n):
    if max(arr) == maximum:
        arr.remove(maximum)

print(max(arr))







