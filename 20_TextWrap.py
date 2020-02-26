import textwrap

def wrap(string, max_width):
    l = textwrap.wrap(string, max_width)
    result = ""
    for i in l:
        result += i
        result += "\n"
    return result


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)


