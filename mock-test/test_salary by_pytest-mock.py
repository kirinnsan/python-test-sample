import pytest

import salary
import dummy


class TestSalary():

    def test_calculation_salary(self, mocker, prepare):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = mocker.patch(
            'salary.ThirdPartryBonusRestAPi.bonus_price',
            side_effect=dummy.dummy_bonus_price)
        assert s.calcuration_salary() == 101
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        assert s.bonus_api.bonus_price.call_count == 1

    def test_calculation_salary_no_salary(self, mocker, prepare):
        s = salary.Salary(year=2030)
        s.bonus_api.bonus_price = mocker.patch(
            'salary.ThirdPartryBonusRestAPi.bonus_price',
            side_effect=dummy.dummy_bonus_price)
        assert s.calcuration_salary() == 100
        s.bonus_api.bonus_price.assert_not_called()


