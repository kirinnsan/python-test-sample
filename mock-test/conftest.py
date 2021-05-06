import pytest


@pytest.fixture()
def prepare():
    print('----------')
    print('start test')
    print('----------')

    yield

    print('----------')
    print('finish test')
    print('----------')
