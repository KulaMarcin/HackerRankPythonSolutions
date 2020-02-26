import datetime as date

m, d, y = input().split()
c = date.datetime(int(y), int(m), int(d))
print(c.strftime("%A").upper())





