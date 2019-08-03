"""
Task solution
"""

def is_leap(year):
    """
    Return True if year is leap otherwise return False
    :param year:
    :return:
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def is_leap_simpler(year):

    if year % 4 == 0:
        if (year % 100 != 0) or (year % 400 == 0):
            return True

    return False

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
    print(is_leap_simpler(year))
