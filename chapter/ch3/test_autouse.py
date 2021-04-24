import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    yield
    now = time.time()
    print('------')
    print(f'finishied:{time.strftime("%d %b %X", time.localtime(now))}')


@pytest.fixture(autouse=True)
def footer_function_scope():
    start = time.time()
    yield
    stop = time.time()
    data = stop - start
    print(f'\ntest duration:{data:.3f} seconds')


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.23)
