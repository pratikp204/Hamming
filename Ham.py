'''

    Author : HackNet & pratikp204

'''
from math import log, floor


def decode(arrout):
    t = enc(arrout)
    j, no, i = 0, 0, 2 ** 0
    while i < len(arrout):
        no += t[i] * i
        j += 1
        i = 2 ** j
    return no


def enc(arrout):
    vax = {}
    for e in range(1, len(arrout)):
        x = e
        if log(e, 2) == floor(log(e, 2)):
            vax[2 ** (floor(log(x, 2)))] = []
        while x > 0 and log(e, 2) != floor(log(e, 2)):
            vax[2 ** (floor(log(x, 2)))].append(e)
            x = x - 2 ** (floor(log(x, 2)))
    for e in vax:
        for y in vax.get(e):
            arrout[int(e)] ^= arrout[y]
    return arrout


def encode(a):
    arrout = []
    i, j = 1, 0
    arrout.append(12)
    while j < len(a):
        if log(i, 2) != floor(log(i, 2)):
            arrout.append(a[j])
            j += 1
        else:
            arrout.append(0)
        i += 1
    z = enc(arrout)
    return z

di = encode([1, 0, 1, 0, 1, 1])
temp = [12, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1]
te=[i for i in temp]
k = decode(temp)
print di[1:]
print k
if k > 0:
    print "Error at location " + str(k)
    if te[k] == 0:
        te[k] = 1
    else:
        te[k] = 0
print te[1:]
