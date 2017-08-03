# 394. Decode String

def decodeString(s):
    if len(s) == 0:
        return s

    strs = []
    times = []

    def find_all_digit(s, i):
        while i < len(s) and s[i].isdigit():
            i += 1
        return i


    cur = ''
    num = 1
    i = 0
    while i < len(s):
        if s[i].isalpha():
            cur += s[i]
            i += 1
        elif s[i].isdigit():
            j = find_all_digit(s, i)
            if j == len(s):
                raise ValueError
            strs.append(cur)
            times.append(num)
            cur = ''
            num = int(s[i:j])
            i = j + 1
        elif s[i] == ']':
            level = cur * num
            cur = strs.pop() + level
            num = times.pop()
            i += 1
    return cur

print decodeString('xt2[cd2[a]]')