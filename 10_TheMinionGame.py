def minion_game(string):
    v = "AEIOU"
    kevin_score, stuart_score = 0, 0
    length = len(string)

    for i in range(length):
        if string[i] in v:
            kevin_score += length - i
        else:
            stuart_score += length - i
    if kevin_score > stuart_score:
        print("Kevin: {0:d}".format(kevin_score))
    else:
        print("Stuart: {0:d}".format(stuart_score))

s = input()
minion_game(s)