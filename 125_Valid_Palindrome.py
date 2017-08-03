# 125. Valid Palindrome

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalpha():
            i += 1
        while i < j and not s[j].isalpha():
            j -= 1
        if i < j and s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


test = "A man, a plan, a canal: Panama"
test2 = '0P'

print isPalindrome(test2)