import pytest


@pytest.fixture()
def some_data():
    # pytest.fixture()デコレータをつけることで
    # その関数がフィクスチャであることをpytestが認識する
    return 11


@pytest.fixture()
def setup():
    print('テストの前処理')

    # ここでテストが実行される
    yield

    # yieldの後の処理は必ず実行される
    print('テストの後処理')


@pytest.fixture()
def return_tuple():
    return (1, 2, 'test1', 'test2', {'dict1': 'bar'})


def test_return_tuple(return_tuple):
    assert return_tuple[0] == 1


def test_some_data(some_data):
    # テスト関数の引数にフィクスチャの名前を指定することで、
    # テストを実行する前にそのフィクスチャがpytestによって実行される
    # 同じ名前のフィクスチャを現在のテスト内のモジュール内で探し
    # 見つからなければ、conftest.pyファイルを見に行く
    assert some_data == 11


def test_setup(setup):
    # setupフィクスチャが呼ばれる
    assert 1 == 1
