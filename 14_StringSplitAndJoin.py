def split_and_join(line):
    new_string = line.split(" ")
    new_string = "-".join(new_string)
    return new_string


line = input()
result = split_and_join(line)
print(result)