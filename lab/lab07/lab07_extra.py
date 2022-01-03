""" Optional Questions for Lab 07 """

from lab07 import *


# Q6
def remove_all(link, value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link.rest == Link.empty:
        return Link.empty
    elif link.rest.first == value:
        link.rest = link.rest.rest
        return remove_all(link, value)
    else:
        return remove_all(link.rest, value)


# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return Link.empty
    if isinstance(link.first, int):
        link.first = fn(link.first)
    elif isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    deep_map_mut(fn, link.rest)  # 如果这里是 return deep_mat_mut(fn, link.rest), return之后就回不到上一层first了？


# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"

    # l = link
    # while link.rest is not Link.empty:
    #     if link.rest == l:
    #         return True
    #     link = link.rest
    # return False

    # Solution 2
    def memory_box(l, cache=[]):
        if l is Link.empty:
            return False
        elif l in cache:
            return True
        else:
            cache.append(l)
        return memory_box(l.rest, cache)

    return memory_box(link)


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # Official solution
    if link is Link.empty:
        return False
    slow, fast = link, link.rest
    while fast is not Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False


# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def reverse_odd(t, need_reverse):
        if t.is_leaf():
            return
        reverse_labels = [child.label for child in t.branches][::-1]
        for i in range(len(t.branches)):
            child = t.branches[i]
            reverse_odd(child, not need_reverse)
            if need_reverse:
                child.label = reverse_labels[i]
    return reverse_odd(t, True)
