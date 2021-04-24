import pytest


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass


def test_1(sess_scope, mod_scope, func_scope):
    pass


def test_2(sess_scope, mod_scope, func_scope):
    pass


@pytest.mark.usefixtures('class_scope')
class TestSomething():

    def test_3(self):
        pass

    def test_4(self):
        pass

# 出力
# chapter/ch3/test_scope.py::test_1
# SETUP    S sess_scope
#     SETUP    M mod_scope
#         SETUP    F func_scope
#         chapter/ch3/test_scope.py::test_1 (fixtures used: func_scope, mod_scope, sess_scope)PASSED
#         TEARDOWN F func_scope
# chapter/ch3/test_scope.py::test_2
#         SETUP    F func_scope
#         chapter/ch3/test_scope.py::test_2 (fixtures used: func_scope, mod_scope, sess_scope)PASSED
#         TEARDOWN F func_scope
# chapter/ch3/test_scope.py::TestSomething::test_3
#       SETUP    C class_scope
#         chapter/ch3/test_scope.py::TestSomething::test_3 (fixtures used: class_scope)PASSED
# chapter/ch3/test_scope.py::TestSomething::test_4
#         chapter/ch3/test_scope.py::TestSomething::test_4 (fixtures used: class_scope)PASSED
#       TEARDOWN C class_scope
#     TEARDOWN M mod_scope
# TEARDOWN S sess_scope
