
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


if __name__ == '__main__':
    print('Employee raise ammount: ', Employee.raise_amount)

    print('')

    emp_1 = Employee('Adam', 'Kunat', 3000)
    print(emp_1.fullname())
    #print(Employee.fullname(emp_1)) --> the same result
    print(emp_1.mail)
    print('Basic:', emp_1.pay)
    emp_1.apply_raise()
    print('Raise:', emp_1.pay)

    print('')

    emp_2 = Employee('Piotr', 'Nowak', 3500)
    print(emp_2.fullname() + ' --- ' + emp_2.mail)
    print('Basic:', emp_2.pay)
    emp_2.raise_amount = 1.05
    #print(Employee.fullname(emp_2) + ' raise ammount:', emp_2.raise_amount)
    print(f'{emp_2.first} {emp_2.last} raise ammount:', emp_2.raise_amount)
    emp_2.apply_raise()
    print('Raise:', emp_2.pay)

    print('')

    print(Employee.__dict__)
    print(emp_1.__dict__)
    print(emp_2.__dict__)

    # Interpreter check the CLASS (Employee) attributes FIRST and assign them to the instance;
    # in other way, if the INSTANCE (emp_2) get own attributes, then Interpreter return result
    # having regard to the change. The place of assignment is important.

    print('')
    print('Number of Employees equals: ', Employee.num_of_emps)

    #The resut is 2 because employees was incremented twice.