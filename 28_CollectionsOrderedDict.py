from collections import OrderedDict

ordered_dictionary = OrderedDict()

N = int(input().strip())

for _ in range(N):
    item_name, s, item_quantity = input().rpartition(' ')
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + int(item_quantity)

for x, y in ordered_dictionary.items():
    print("%s %d" % (x, y))





