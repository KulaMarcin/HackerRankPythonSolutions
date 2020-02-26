import collections

l = collections.Counter(input() for _ in range(int(input())))
s = set(l)
number_of_occurences = " ".join(str(i) for i in l.values())

print(len(s))
print(number_of_occurences)
