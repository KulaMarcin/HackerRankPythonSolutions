import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase
    AR = []

    for i in range(size):
        first_part = "-".join(alphabet[i:size])
        AR.append((first_part[::-1]+first_part[1:]).center(4*size-3, "-"))

    print("\n".join(AR[:0:-1]+AR))


n = int(input())
print_rangoli(n)