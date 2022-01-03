""" Optional problems for Lab 6 """


# Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    turn = 0

    def take_turn():
        nonlocal turn
        turn += 1
        return str(snacks[(turn - 1) % len(snacks)])

    return take_turn
