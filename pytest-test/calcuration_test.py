import os
import shutil

import pytest

import calcuration

is_release = False


class Test:

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calcuration.Cal()
        cls.test_dir = 'test_dir'
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setup_method(self, method):
        print(f'method={method.__name__}')
        # self.cal = calcuration.Cal()

    def teardown_method(self, method):
        print(f'method={method.__name__}')

    @pytest.mark.skipif(is_release, reason='skip')
    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double(5, '5')

    def test_no_dirctory(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
