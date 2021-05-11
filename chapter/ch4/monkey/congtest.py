import pytest


@pytest.fixture()
def prepare():
    print('start test')

    yield

    print('finish test')
