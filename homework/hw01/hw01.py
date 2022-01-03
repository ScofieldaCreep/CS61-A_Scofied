from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a * a + b * b + c * c - min(a, b, c) ** 2
    # 1st = sorted([a, b, c])[-2:]
    # res = 0
    # for i in 1st:
    #       res += i * i
    # return res


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """

    i = 1
    while i <= n ** (1 / 2):  # 10 * 1/2 = 5.0; 10 ** (1/2) == 3.16...
        i += 1
        if not n % i:
            return n // i
    return 1


# ！！！
""" 首先需要考虑为何会出现这样的不同。原因在于对函数求值时，需要先对函数的全部参数进行求值。
    with_if_statement() 是一个正常的 if 调用流程，根据 cond() 的布尔值不同，true_func() 和 false_func() 二者中有且仅有一个函数会被执行。
    with_if_function() 中涉及到了函数调用，cond()，true_func()，false_func() 三者作为 if_function() 的参数，在实际计算 if_function()
时上述的三个函数都被先行计算了。
    接下来需要考虑如何实现题目中的要求。有一点可以肯定，即 true_func() 和 false_func() 都不能是 pure function，否则的话由于 pure function
没有 side effect 的特性，with_if_statement() 和 with_if_function() 的实际外部表现并不会有所不同。"""
# with_if_statement只能返回函数f()的返回值， 而with_if_function 可以返回f()的同时，运行t()的内容(莫名觉厉！！！)


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()


def with_if_function():
    return if_function(c(), t(), f())


def c():
    return False


def t():
    print('t()被打印')
    print(42)
    return None


def f():
    return 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

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
    i = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
            # 如果这里写'n /= 2'，之后的n都会带一个小数位
        else:
            n = 3 * n + 1
        i += 1
    print(1)
    return i

