""" Lab 3: Recursion and Midterm Review """


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    # if max(a, b) % min(a, b) == 0:
    #     return min(a, b)
    # else:
    #     return gcd(min(a, b), max(a, b) % min(a, b))

    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

    # if b % a == 0:
    #     return a
    # elif a < b:
    #     return gcd(b, a)
    # else:
    #     return gcd(a - b, b)

    # def divisor(n):
    #     if a % n == 0 and b % n == 0:
    #         return True
    #     return False
    # n = 2
    # max_divisor = 1
    # while n <= a and n <= b:
    #     if divisor(n):
    #         max_divisor = n
    #     n += 1
    # return max_divisor


# hin牛逼！！！ 记住recursion需要return
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)

    # 我一开始这么写的， 这样每一次开始num都重新初始化为0，就没法计算了
    # print(n)
    # if n == 1:
    #     return num
    # if n % 2 == 0:
    #     hailstone(n // 2)
    # else:
    #     hailstone(n * 3 + 1)
    