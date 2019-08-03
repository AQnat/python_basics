"""
For loop
"""


def premature_lift_off(number):
    while number:
        print(number)
        number -= 1
        if number == 0:
            print('Lift off!!')
            break


if __name__ == '__main__':
    premature_lift_off(10)
