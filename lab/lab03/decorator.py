def trace1(fn):
    """Returns a version of fn that first printed when it is called.

    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument:', x)
        return fn(x)
    return traced


def square(x):
    return x * x


square = trace1(square)
print(square(5))


@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k < n:
        total, k = total + square(k), k + 1
    return total
