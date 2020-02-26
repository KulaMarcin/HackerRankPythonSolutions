N = int(input())
countries = set()

for _ in range(N):
    countries.add(input().strip())

print(len(countries))