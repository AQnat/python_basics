import datetime
import os
import unittest
import sys

from unittest import mock

from src.employee import Employee, Developer, Manager


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('Jan', 'Testowy', 3000)

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

    @unittest.skip('To be updated')
    def test_if_workday(self):
        workday = datetime.date(2019, 7, 12)
        weekend = datetime.date(2019, 7, 13)
        self.assertTrue(
            Employee.is_workday(workday)
        )
        self.assertFalse(
            Employee.is_workday(weekend)
        )

    def test_read_env_var(self):
        self.assertEqual(
            'ABC',
            os.environ['TEST_VARIABLE']
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


class RepoMock:
    pass

class DeveloperTestCase(unittest.TestCase):

    @mock.patch('src.github_api.GithubApi.get_user_repositories')
    def test_getting_repos(self, mock_get_user_repositories):
        dev = Developer('Jan', 'Bo', 2000, 'python', 'lonicram')
        repo_mock = RepoMock()
        repo_mock.name = 'test/repo'
        mock_get_user_repositories.return_value = [repo_mock]
        repos = dev.get_github_repositories()
        mock_get_user_repositories.assert_called_with(
            dev.github_login
        )


if __name__ == '__main__':
    unittest.main()