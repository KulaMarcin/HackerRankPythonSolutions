def solve(string):
    for x in string.split():
        string = string.replace(x, x.capitalize())
    return string


string = input()
x = solve(string)
print(x)
