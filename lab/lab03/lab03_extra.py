""" Optional problems for Lab 3 """

from lab03 import *


## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """

    # def nested(n):
    #     def outcome(x):
    #         nonlocal n
    #         res = x
    #         while n > 3:
    #             res = f3(f2(f1(res)))
    #             n -= 3
    #         if n == 0:
    #             res = res
    #         elif n == 1:
    #             res = f1(res)
    #         elif n == 2:
    #             res = f2(f1(res))
    #         else:
    #             res = f3(f2(f1(res)))
    #         return res
    #     return outcome
    # return nested
    #
    def cycle_n(n):
        def cycle_m(m):
            i, res = 0, m
            func_lst = [f1, f2, f3]
            while i < n:  # 如果这里写一个 n -= 3 就会报错，内层函数不能修改外层函数的变量，除非加上nonlocal修饰
                ind = i % 3
                res = func_lst[ind](res)
                i += 1
            return res

        return cycle_m

    return cycle_n


## Lambda expressions
## 太妙啦！！！
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n


## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    stan = n // 2 + 1

    def helper(i):
        if i == stan:
            return True
        if n % i:
            i += 1
            return i

    return helper(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    # My solution
    # def helper(i):
    #     total = 0
    #     if i == 0:
    #         return 0
    #     elif i == 1:
    #         return odd_term(1)
    #     elif i == 2:
    #         return odd_term(1) + even_term(2)
    #     else:
    #         if n % 2 == 0:
    #             return even_term(n) + odd_term(n - 1) + interleaved_sum(n - 2, odd_term, even_term)
    #         else:
    #             return odd_term(n) + even_term(n - 1) + interleaved_sum(n - 2, odd_term, even_term)
    # return helper(n)

    # Solution 2
    # def helper(i):
    #     if i + 1 <= n:  # 从1开始加，i + 1 <= n 确定能够加odd_term(i)和even_term(i+1)，同时i + 2可以调用helper进行recursion
    #         return odd_term(i) + even_term(i + 1) + helper(i + 2)
    #     elif i <= n:  # 如果条件 i + 1 <= n 不成立了，就进行这一步，需要确保最后一个helper调用能够成功(即n为奇数情况下的最后一个被加数)
    #         return odd_term(i)
    #     else:
    #           return 0
    # return helper(1)

    # Solution 3
    # f1和f2在每次迭代的时候对换，hin帅！！！
    def helper(f1, f2, k):
        if k == n:
            return f1(k)
        return f1(k) + helper(f2, f1, k + 1)

    return helper(odd_term, even_term, 1)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(last, leave):
        if last == 0:
            return 0
        elif last % 10 == leave:
            return 1 + helper(last // 10, leave)
        else:
            return helper(last // 10, leave)
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + helper(n // 10, 10 - n % 10)

    # The question asks not to use the assignment.
    # Solution 2
    # res = 0
    # num = 0
    # x = n
    # while n != 0:
    #     n, last = n // 10, n % 10
    #     x = n
    #     while x:
    #         if x % 10 + last == 10:
    #             num += 1
    #         x = x // 10
    #
    # return num

    # Solution 3
    # def helper(n, last):
    #     if n == 0:
    #         return 0
    #     else:
    #         if n % 10 == last:
    #             return 1 + helper(n // 10, last)
    #         else:
    #             return helper(n // 10, last)
    # res = 0
    # for i in range(1,5):
    #     res += helper(n, i) * helper(n, 10 - i)
    # res += helper(n, 5) * (helper(n, 5) - 1) // 2
    # return res