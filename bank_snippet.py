"""
Są dwie klasy: Account i Card.
Odwołanie się do obiektu Account powinno zwracać numer konta.
Metoda Account.owner powinna zwracać Imię  i nazwisko właściciela.
Metoda Account.balance powinna zwracać aktualny stan konta.
Metoda Account.number powinna zwracać numer konta.
Metoda Account.transfer powinna zmieniać stan konta o podaną kwotę
Odwołanie się do obiektu Card powinno zwracać imie i nazwisko właściciela konta.
Metoda Card.check_pin powinna sprawdzić czy pin jest poprawny.
Metoda Card.get_account powinna zwrócić konto do którego karta jest „podpięta”
​
"""
import random

class Account:
    def __init__(self, number, first_name, last_name, balance=0):
        self._balance = balance
        self._number = number
        self.first_name = first_name
        self.last_name = last_name

    @property
    def owner(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    def transfer(self, amount):
        self._balance += amount

    def __str__(self):
        return f'Account({self._number})'

class Card:
    def __init__(self, account: Account):
        self._account = account
        self._pin = random.sample(range(10), 5)

    def __str__(self):
        return f'{self._account.owner}'

    def check_pin(self, pin):
        return pin == self._pin

    def get_account(self):
        return self._account

class SomeClass:
    def hello(self):
        return 'hello'
