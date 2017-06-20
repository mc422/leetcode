
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowel_list = ['a', 'e', 'u', 'i', 'o', ]
    s = list(s)
    length = len(s)
    if length == 0:
        return ''
    start, end = 0, length-1
    while start < end:
        while start < length and s[start] not in vowel_list:
            start += 1
        while end >= 0 and s[end] not in vowel_list:
            end -= 1
        if start < end:
            s[start], s[end] = s[end], s[start]
    return ''.join(s)


print reverseVowels('hello world')
