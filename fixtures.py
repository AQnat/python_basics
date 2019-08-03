import unittest
import datetime
from src.employee import Employee, Manager


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('Jan', 'Testowy', 3000)
        print(
            'Initializing Employee Test object ',
        )

    def test_applying_raise_amount(self):
        """Test applying raise on Employee"""
        emp = self.emp
        initial_pay = emp.pay
        self.assertEqual(emp.pay, initial_pay)
        emp.apply_raise()
        self.assertTrue(emp.pay > initial_pay)
        self.assertGreater(emp.pay, initial_pay)

        expected_pay = initial_pay * emp.raise_amount
        self.assertEqual(emp.pay, expected_pay)

    def test_property_fullname(self):
        emp = self.emp
        self.assertEqual('Jan Testowy', emp.fullname)
        emp.fullname = 'Jan Nowak'
        self.assertEqual('Jan', emp.first)
        self.assertEqual('Nowak', emp.last)

    def test_if_workday(self):
        workday = datetime.date(2019, 7, 12)
        weekend = datetime.date(2019, 7, 13)
        self.assertTrue(
            Employee.is_workday(workday)
        )
        self.assertFalse(
            Employee.is_workday(weekend)
        )

class ManagerTestCase(unittest.TestCase):
    """"""
    def setUp(self):
        self.emp1 = Employee('Jan', 'Bo', 2000)
        self.emp2 = Employee('Zenon', 'Nowak', 2000)
        self.mng = Manager(
            'Zdzisław', 'Iksiński', 2000, employes=[self.emp1, ]
        )

    def test_adding_employees(self):
        emp1, emp2, mng = self.emp1, self.emp2, self.mng
        self.assertEqual(mng.employes, {emp1})

        mng.add_employee(emp2)
        self.assertEqual(mng.employes, {emp1, emp2})

    def test_removing_employees(self):
        emp1, emp2, mng = self.emp1, self.emp2, self.mng
        mng.remove_employee(emp1)
        self.assertFalse(mng.employes)


if __name__ == '__main__':
    unittest.main()