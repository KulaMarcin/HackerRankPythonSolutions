import re

n = input()

for _ in range(int(n)):
    name, email = input().split(" ")
    match = re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", email)
    if match:
        print(name, email)