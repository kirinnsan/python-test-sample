import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartryBonusRestAPi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calcuration_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2030)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calcuration_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('salary.ThirdPartryBonusRestAPi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with_version(self):
        with mock.patch(
                'salary.ThirdPartryBonusRestAPi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calcuration_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def test_calculation_salary_patch_with_patcher(self):
        # patcher = mock.patch('salary.ThirdPartryBonusRestAPi.bonus_price')
        # mock_bonus = self.patcher.start()
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

        # self.patcher.stop()

    def test_calculation_salary_patch_with_side_effect(self):
        # def f(year):
        #     return year * 2

        self.mock_bonus.side_effect = ConnectionRefusedError

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 100)
        self.mock_bonus.assert_called()

    @mock.patch('salary.ThirdPartryBonusRestAPi', spec=True)
    def test_calculation_salary_class(self, mock_rest):
        mock_rest = mock_rest.return_value
        # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()

    def test_mock_confirm(self):
        test_mock = mock.Mock()
        test_mock().foo(a=2, b=3)

        test_mock.return_value.foo.assert_called_with(a=2, b=3)

    # def test_get_max_salary(self):
    #     max_salary_mock = mock.Mock()
    #     res_mock = mock.Mock()
    #     s = salary.Salary(year=2017)
    #     max_salary_mock.return_value.last_three_salary_list.return_value.max_salary.return_value = res_mock
    #     s.bonus_api = max_salary_mock

    #     s.get_max_salary()
    #     res_mock.assert_called_once()