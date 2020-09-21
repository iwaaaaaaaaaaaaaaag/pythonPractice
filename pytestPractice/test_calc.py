#実行方法
#pytest test_calc.py -s --os-name=windows

import calc
import pytest


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calc.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal


    def setup_method(self, method):
        print('medhod={}'.format(method.__name__))
        #self.cal = calc.Cal()

    def teardown_method(self, method):
        print('medhod={}'.format(method.__name__))
        #del self.cal

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    @pytest.mark.skip(reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1','1')

