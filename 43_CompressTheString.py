from itertools import groupby

string = input()

pairs = [(len(list(c)), int(s)) for s, c in groupby(string)]

print(*pairs)
