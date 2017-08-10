
# def multiply(a, b):
	# return a * b

# if __name__=='__main__':
	# import doctest
	# doctest.testmod(verbose=True)

# multiply(4, 3)
# multiply('a', 3)
'''
'''
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a + b
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)