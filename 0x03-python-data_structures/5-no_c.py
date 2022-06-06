def no_c(my_string):
    new = my_string[:]

    while 'c' in new:
        new.remove('c')
    while 'C' in new:
        new.remove('C')

    return new
