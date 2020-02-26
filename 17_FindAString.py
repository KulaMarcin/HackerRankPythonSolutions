import re

def count_substring(string, sub_string):
    quantity = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            quantity += 1
    return quantity


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)