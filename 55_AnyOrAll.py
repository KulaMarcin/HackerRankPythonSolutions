N = int(input())
array = input().split()

print(all(int(i)>=0 for i in array) and any(i == i[::-1]for i in array))