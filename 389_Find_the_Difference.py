# 389. Find the Difference
# convert char to int and use bit mapulation to calcuate different of 2 string

def findTheDifference(s, t):
    d = 0
    for i in s:
        d ^= ord(i)
    for i in t:
        d ^= ord(i)
    return chr(d)


print findTheDifference('abdaef', 'abdaaef')