
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    def cal(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n /= 10
        return sum

    visited = set()
    while n != 1:
        target = cal(n)
        if target in visited:
            return False
        visited.add(target)
        n = target
    return True

print isHappy(100)
