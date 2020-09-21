import unittest
import calcration

release_name = 'lesson'

class CalTest(unittest.TestCase): #unittest.TestCaseを継承
    #テスト実行前に実行されるもの
    def setUp(self):
        print('setup')
        self.cal = calcration.Cal()

    #テスト実行後に実行されるもの
    def tearDown(self):
        print('clean up')
        del self.cal

    #unittestのスキップ
    #@unittest.skip('skip')
    @unittest.skipIf(release_name=='lesson', 'skip')
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1),4)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()