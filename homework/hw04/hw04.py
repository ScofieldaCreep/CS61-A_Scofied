HW_SOURCE_FILE = 'hw04.py'


###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st + ave) * (st + ave + 1) // 2 + ave


def street(inter):
    return w(inter) - avenue(inter)


def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2


w = lambda z: int(((8 * z + 1) ** 0.5 - 1) / 2)


def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    # My solution
    # outcome = []
    # for i in s:
    #     if pow(round(i ** 0.5), 2) == i:
    #         # outcome = outcome + [int(i ** 0.5)]
    #         outcome.append(round(i ** 0.5))
    # return outcome

    # Official Solution
    return [round(i ** 0.5) for i in s if round(i ** 0.5) ** 2 == i]


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


# 太难了太难了-.-
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    # i = 3
    # num1, num2, num3 = 1, 2, 3
    # if n <= 3:
    #     return n
    # else:
    #     while i < n:
    #         num1, num2, num3 = num2, num3, num1 + 2 * num2 + 3 * num3
    #         i += 1
    #     return num3

    # Cool Solution!
    if n <= 3:
        return n
    else:
        prev = [1, 2, 3]
        cur = 0
        while n > 3:
            cur = 3 * prev[0] + 2 * prev[1] + 1 * prev[2]
            prev = [prev[1], prev[2], cur]
            n -= 1
        return cur


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def pingpong_next(k, p, up_status):
        if k == n:
            return p
        elif up_status:
            return pingpong_switch(k + 1, p + 1, up_status)
        else:
            return pingpong_switch(k + 1, p - 1, up_status)

    def pingpong_switch(k, p, up_status):
        if k % 7 == 0 or has_seven(k):
            return pingpong_next(k, p, not up_status)
        else:
            return pingpong_next(k, p, up_status)
    return pingpong_next(1, 1, up_status=True)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def max_cent(n):
        i = 1
        while i < amount:
            i *= 2
        return i // 2
    # My Solution
    # def count_partitioner(amount, max_cent):
    #     # 这个为啥也行？？？
    #     # if max_cent == 1:
    #     #     return 1
    #     # elif amount == 0:
    #     #     return 1
    #     # elif amount < 0:
    #     #     return 0
    #     if amount == 0:
    #         return 1
    #     elif max_cent == 1:
    #         return 1
    #     elif amount < 0:
    #         return 0
    #     else:
    #         return count_partitioner(amount - max_cent, max_cent) + count_partitioner(amount, max_cent // 2)
    #
    # return count_partitioner(amount, max_cent(amount))

    # Official Solution
    def count_using(min_coin, amount):
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        elif min_coin > amount:
            return 0
        else:
            return count_using(min_coin, amount - min_coin) + count_using(min_coin * 2, amount)

    return count_using(1, amount)

# Reference
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 1:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return count_partitions(n - m, m) + count_partitions(n, m - 1)


###################
# Extra Questions #
###################

from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda x: f(f, x))(lambda f, x: x if x == 1 else mul(f(f, sub(x, 1)), x))

    # return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(f(f, sub(k, 1)), k))
