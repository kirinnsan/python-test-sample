import pytest
from human_model import HumanModel, Human


class TestHuman:
    """クラスのモック化のテスト"""

    def test__regist(self, mocker):
        # HumanModelをモック
        # insert、updateもモック化される
        h_model = mocker.Mock(spec=HumanModel)
        mocker.patch('human_model.HumanModel', return_value=h_model)

        # 実行
        human = Human()
        human._regist()

        # メソッド呼び出しを確認
        h_model.insert.assert_called()
        # 登録値を確認
        assert h_model.name == 'taro'
        assert h_model.age == 20
        assert h_model.sex == '男'

    def test__update(self, mocker):
        # HumanModelをモック
        # insert、updateもモック化される
        h_model = mocker.Mock(spec=HumanModel)
        mocker.patch('human_model.HumanModel', return_value=h_model)

        # 実行
        human = Human()
        human._update()

        # メソッド呼び出しを確認
        h_model.insert.assert_called()
        h_model.update.assert_called()

        # 登録値を確認
        assert h_model.name == 'kaoru'
        assert h_model.age == 23
        assert h_model.sex == '女'
