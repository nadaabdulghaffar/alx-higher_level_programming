#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    elm = 0
    try:
        while elm < x:
            print("{:d}".format(my_list[elm]), end=' ')
            count += 1
            elm += 1
    except (ValueError, TypeError, IndexError):
        pass

    print()
    return count
