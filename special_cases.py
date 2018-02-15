""" 
This file contain some special cases, in which people might misunderstand python
"""


def special_case_of_rangefunction():
    """ range(1,1,-1) return empty list"""
    r1 = list(range(1, 1, -1))
    # would you expect r1=[0]?"""
    print("r1=", r1)
    
    r2 = list(range(1, 1))
    # why r2 does not contain 1?
    print("r2=", r2)


if __name__ == '__main__':
    special_case_of_rangefunction()
