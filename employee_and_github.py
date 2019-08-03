"""
Employee classes
"""
import datetime
from src.github_api import GithubApi

class Employee:
    """Represents an employee"""
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @property
    def email(self):
        return f'{self.first}.{self.last}@example.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)

    def __str__(self):
        return f'{self.fullname}'

    #def __repr__(self):
        #return f'{self.__class__} {self.fullname} {self.email}'

class Tester(Employee):
    raise_amount = 1.15
    mode = 'manual'

    @property
    def email(self):
        return f'{self.first[0]}.{self.last}@example.com'

class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, first, last, pay, programming_language, github_login):
        super().__init__(first, last, pay)
        self.programming_language = programming_language
        self.github_login = github_login

    def get_github_repositories(self):
        ga = GithubApi()
        repos = ga.get_user_repositories(self.github_login)
        return [repo.name for repo in repos]

    def get_github_topics(self):
        pass

    def get_github_stats(self):
        pass



class Manager(Employee):
    def __init__(self, first, last, pay, employes=None):
        super().__init__(first, last, pay)
        if employes is None:
            self.employes = set()
        else:
            self.employes = set(employes)

    def add_employee(self, employee):
        self.employes.add(employee)

    def remove_employee(self, employee):
        self.employes.remove(employee)

    def print_employees(self):
        print(self.employes)

def foo():
    print('foo')
    def bar():
        print('bar')

if __name__ == '__main__':
    print('main block')
    tester = Tester('Jan', 'Nowak', 3000)