"""
Employee class
"""

import datetime


class Employee:
        """
        Represents an employee
        """
        raise_amount = 1.04

        """
        The basic atributes for Employee
        """
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = f'{first}.{last}@example.com'

        def fullname(self):
            return f'{self.first} {self.last}'

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

        """
        Class methods
        """
        @classmethod
        def set_raise_amount(cls, new_new_raise_amount):
            cls.raise_amount = new_new_raise_amount

        @staticmethod
        def is_workday(day):
            return day.weekday() not in (5, 6)

if __name__ == '__main__':
    today = datetime.date.today()
    # day = today + datetime.timedelta()
    print('Is workday? ', Employee.is_workday(today))