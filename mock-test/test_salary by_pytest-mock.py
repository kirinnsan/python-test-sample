import pytest
from unittest import mock
from unittest.mock import patch
import os
import datetime

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
        path_mocker = mocker.patch(
            'os.path.join', return_value='test/sample.txt')

        ss = os.path.join('test1/test2', 'test.txt')
        print('sssssssssssssssssssssssss')
        print(ss)
        print(path_mocker)
        print('sssssssssssssssssssssssss')
        path_mocker.assert_called()
        assert ss == 'test/sample.txt'

    def test_datetime_mock(self, mocker):
        from datetime import datetime
        import time

        # salary.pyのdatetime.now()をモック化

        # 1.unittestのmockを使用したパターン
        # with patch('salary.datetime') as datetime_mock:
        #     datetime_mock.now.return_value = datetime(2019, 1, 1, 10, 11, 20)
        #     datetime_mock.utcnow.return_value = datetime(2019, 1, 1, 1, 11, 20)
        #     s = salary.Salary()
        #     datetime_now = s.now_date_time()
        #     datetime_now_utc = s.now_date_time_utc()
        # assert datetime_now == "name_2019-01-01 10:11:20"
        # assert datetime_now_utc == "name_2019-01-01 01:11:20"

        # 2.pytest-mockを使用したパターン
        datetime_mock = mocker.patch('salary.datetime', mocker.Mock())
        datetime_mock.now.return_value = datetime(2019, 1, 1, 10, 11, 20)
        datetime_mock.utcnow.return_value = datetime(2019, 1, 1, 1, 11, 20)

        # time.time()をモック化
        mocker.patch('time.time', mocker.Mock(return_value=10))

        s = salary.Salary()
        datetime_now = s.now_date_time()
        datetime_now_utc = s.now_date_time_utc()
        time_now = s.now_time()
        datetime_method_cain = s.datetime_method_cahin()

        assert datetime_now == "name_2019-01-01 10:11:20"
        assert datetime_now_utc == "name_2019-01-01 01:11:20"
        assert time_now == "name_10"
        assert datetime_method_cain == "name_2019-01-01"
