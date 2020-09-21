import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary

#APIをmock化
class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salaly(year=2017)

        s.bonus_api.bonus_price = MagicMock(return_value=1)#mock化
        self.assertEqual(s.calculation_salary(), 101)

        s.bonus_api.bonus_price.assert_called()#実際に呼ばれたかどうかを確認する
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)


    def test_calculation_salary_no_salary(self):
        s = salary.Salaly(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)#mock化
        self.assertEqual(s.calculation_salary(), 100)

        s.bonus_api.bonus_price.assert_not_called()#実際に呼ばれたかどうかを確認する

    #インスタンス化する前にモック化する方法
    #デコレータを使う
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    #インスタンス化する前にモック化する方法
    #with句を使う
    #使い時：テスト内でモックにしたい時としたくない時を分けたい場合
    def test_calculation_salary_patch2(self):
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salaly(year=2010)
            salary_price = s.calculation_salary()
            
            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()


    #インスタンス化する前にモック化する方法
    #patcherを使う 
    #使い時：setupで一括でモックしたい時
    def test_calculation_salary_patch_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()
            
        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    #モック化した関数を自由に書き換える事ができる
    def test_calculation_salary_patch_side_effect(self):
        #def f(year):
        #    return 1
        #self.mock_bonus.side_effect = ConnectionRefusedError 

        #複数回呼ばれた時に挙動を戻り値を変えることも可能
        self.mock_bonus.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!!!!')
        ]

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)

        s = salary.Salaly(year=2010)
        with self.assertRaises(ValueError):
            s.calculation_salary()


    #classごとモックにする
    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    def test_calculation_salary_class(self, MockRest):
        mock_rest = MockRest.return_value #こっちの方が推奨されている書き方らしい
        #mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()

    #複数をモック化
    #デコレータの下が、引数の左になる
    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    @mock.patch('salary.Salary.get_from_boss')
    def test_calculation_salary_class2(self ,mock_boss ,MockRest):
        mock_boss.return_value = 10
        mock_rest = MockRest.return_value #こっちの方が推奨されている書き方らしい
        #mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1

        s = salary.Salaly(year=2010)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 11ｘｘｘｘｘ1)
        mock_rest.bonus_price.assert_called()


    #関数もモック化できる
    @mock.patch('salary.hoge')
    def test_hoge(self, mock):
        mock.return_value = "fuga"
        self.assertEqual(salary.hoge(),"fuga")
    
if __name__ == '__main__':
    unittest.main()