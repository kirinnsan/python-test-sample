import pytest
from unittest import mock
import os

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

    def test_patch_object_method(self, mocker, prepare):
        """インスタンスメンバのメソッドをモック化"""
        s = salary.Salary()
        mocker.patch.object(s, 'calcuration_heavy_task', return_value=500)

        result = s.calcuration_bonus()
        assert result == 600

    def test_patch_object_variable(self, mocker, prepare):
        """インスタンス変数をモック化"""
        s = salary.Salary()
        mocker.patch.object(s, 'base', 400)
        mocker.patch.object(s, 'calcuration_heavy_task', return_value=500)

        result = s.calcuration_bonus()
        assert result == 900

    def test_path(self, mocker):
        path_mocker = mocker.patch('os.path.join', return_value='test/sample.txt')

        ss = os.path.join('test1/test2', 'test.txt')
        print('sssssssssssssssssssssssss')
        print(ss)
        print(path_mocker)
        print('sssssssssssssssssssssssss')
        path_mocker.assert_called()
        assert ss == 'test/sample.txt'

    # def test_local_variablea(self, mocker):
    #     with mock.patch('salary.Salary.outer') as mo:
    #         s = salary.Salary()
    #         mo.return_value.inner.return_value = 'bbb'
    #         result = s.outer('aaa')
    #         # mo.assert_called()
    #         assert result == 'bbb'