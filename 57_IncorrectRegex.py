import re

for _ in range(int(input())):
    regex_is_correct = True
    try:
        regex = re.compile(input())
    except re.error:
        regex_is_correct = False
    print(regex_is_correct)