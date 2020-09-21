class Person(object):
    #コンストラクタ
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print('hello')
        self.run()
    
    def run(self):
        print('run')
    
    #デストラクタ
    def __del__(self):
        print('good bye')

person = Person('aaaaaaaaaa') #インスタンス化
person.say_something()

del person

print('##################')



# クラスの継承
class Car(object):
    def __init__(self, model=None):
        self.model = model
        
    def run(self):
        print('run')

class ToyotaCar(Car):
    def __init__(self, model=None):
        super().__init__(model) #親を呼び出す

class TeslaCar(Car):
    def __init__(self, model=None, enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def auto_run(self):
        if self.enable_auto_run:
            print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar('Model S' ,True)
print(tesla_car.model)
tesla_car.auto_run()


#getter setterの設定
class Hoge(object):

    def __init__(self,test='test'):
        self.__test = test

    def hello(self):
        print('in class  self.__test : {} '.format(self.__test))#中からは参照できる

    @property
    #getter
    def test(self):
        return self.__test

    @test.setter
    #setter
    def test(self, var):
        self.__test = var

hoge = Hoge()
hoge.hello()
print(hoge.test)
hoge.test = 'aaa'
print(hoge.test)
print(hoge.__test)#外からは参照できない


#抽象クラス
import abc
class Piyo(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Paon(Piyo):
    def __init__(self):
        super().__init__()

    def drive(self):
        print('abstract method!')

paon = Paon()
paon.drive()


#多重継承
class test1(object):
    def talk(self):
        print('talk')

class test2(object):
    def run(self):
        print('run')

class test3(test1,test2):
    def fly(self):
        print('fly')

aa = test3()
aa.talk()
aa.run()
aa.fly()

#クラス変数
#！全てのオブジェクトで共有されることに注意！
class T(object):
    word = []
    def add_word(self,word):
        self.word.append(word)

c = T()
c.add_word(1)
c.add_word(2)
print(c.word)

d = T()
d.add_word(3)
d.add_word(4)
print(d.word)


#クラスメソッド、スタティックメソッド
#オブジェクトを作成しなくてもメソッドを実行できる
class aaa(object):
    a = 'hoge'

    @classmethod
    def hello(cls):
        print('hello!!!! {}'.format(cls.a))


    @staticmethod
    def hello2(aa):
        print('hello!!!! {}'.format(aa))

bbb = aaa()
bbb.hello()
aaa.hello()
aaa.hello2('aaa')