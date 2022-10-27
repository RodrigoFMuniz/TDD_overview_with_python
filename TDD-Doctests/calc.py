def soma(x, y):
    '''
    soma s e y

    >>> soma(1,2)
    3
    
    >>> soma(5,2)
    7
    
    >>> soma(10,2)
    12

    >>> soma('1',2)
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    '''
    return x+y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)