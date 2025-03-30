with open("LIST.INP") as filein:
    a = list(map(int, filein.read().strip().split(" ")))

s = 0
while a:
    indexmin = a.index(min(a))
    s += (len(a) - indexmin)*3*min(a)
    a = a[:indexmin]
print(s)