# 439	Ternary Expression Parser

# use string iteration
def tenary_parser1(s):
    BOOL_MAP = {
        'T': True,
        'F': False
    }

    if not s:
        return None

    def dfs(s, i):
        # return res and index
        if i >= len(s):
            return None, i
        res = 0
        cond = s[i]
        i += 2
        if i>=len(s):
            return None, i
        left = s[i]
        if not left.isdigit() and s[i+1] == '?':
            left, i = dfs(s, i)
        i += 2
        if i>=len(s):
            return None, i
        right = s[i]
        if not right.isdigit() and s[i+1] == '?':
            right, i = dfs(s, i)
        res = left if BOOL_MAP.get(cond) else right
        return res, i

    ans = dfs(s, 0)
    return ans

test = 'T?F?T?1:2:3:4'
print tenary_parser1(test)


def tenary_parser2(s):
    if not s:
        return None

    ls = len(s)
    stack = []
    i = ls-1
    while i>=0:
        if s[i] == '?':
            cond = s[i-1]
            left = stack.pop()
            stack.pop()
            right = stack.pop()
            value = left if cond == 'T' else right
            stack.append(value)
            i -= 2
        else:
            stack.append(s[i])
            i -= 1
    return stack[-1]

test = "T?T?F:5:3"
print tenary_parser2(test)

