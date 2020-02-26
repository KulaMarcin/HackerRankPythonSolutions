any_alphanumeric_character = False
any_alphabetical_character = False
any_digits = False
any_lowercase_character = False
any_uppercase_character = False

string = input().strip()

for i in string:
    if i.isalnum():
        any_alphanumeric_character = True
    if i.isalpha():
        any_alphabetical_character = True
    if i.isdigit():
        any_digits = True
    if i.islower():
        any_lowercase_character = True
    if i.isupper():
        any_uppercase_character = True

print(any_alphanumeric_character)
print(any_alphabetical_character)
print(any_digits)
print(any_lowercase_character)
print(any_uppercase_character)