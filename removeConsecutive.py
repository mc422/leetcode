
def removeConsecutive(s):
    i, j = 0, 0
    while i < len(s):
        if s[i] == s[j]:
            i += 1
        elif i-j>=3:
            return removeConsecutive(s[0:j]+s[i:])
        else:
            j = i
    if i-j>=3:
        s = s[0:j]
    return s

def analyse(s):
    i, j = 0, 0
    one, two = [], []
    while i < len(s)+1:
        if i<len(s) and s[i] == s[j]:
            pass
        else:
            if i-j == 1:
                one.append(i)
            else:
                two.append(i)
            j = i
        i += 1
    return one, two

test = 'aabbccaaa'
print removeConsecutive(test)

test = 'aabccbbaad'
print analyse(test)