def convert(s):
    r = [ord('a'), ord('z')]
    new_s = ''
    shift = ord('a') - ord(s[0])
    for i in range(len(s)):
        s_d = ord(s[i]) + shift
        if s_d < r[0]:
            s_d = r[1] - (r[0] - s_d - 1)
        new_s += chr(s_d)
    return new_s

print convert('yu')
print convert('cy')