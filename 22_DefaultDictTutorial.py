from collections import defaultdict

N, M = map(int, input().split())
def_dict = defaultdict(list)

for i in range(1, N + 1):
    def_dict[input()].append(str(i))
for i in range(M):
    print(' '.join(def_dict[input()]) or -1)