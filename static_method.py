import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    """
    The basic atributes for Employee
    """
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f'{first}.{last}@example.com'.lower()

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def new_emp(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'This day is not a workday'
        return 'This day is a workday'


if __name__ == '__main__':

    emp_1 = Employee('Adam', 'Kunat', 3000)
    emp_2 = Employee('Piotr', 'Nowak', 3500)
    emp_str_1 = 'Paweł-Nowak-4500'
    emp_str_2 = 'Tadeusz-Baran-4800'

    new_emp_1 = Employee.new_emp(emp_str_1)
    print(new_emp_1.fullname())
    print(new_emp_1.mail)
    print(new_emp_1.pay)
    Employee.set_raise_amount(1.05)
    new_emp_1.apply_raise()
    print(new_emp_1.pay)

    my_date = datetime.date(2019, 7, 26)
    print(Employee.is_workday(my_date))