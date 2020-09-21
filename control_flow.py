# if文
a = 10
if a > 0:
    print("positive")

# in関数
y = [1,2,3]
x = 1
if x in y:
    print('in')

if '100' not in y:
    print('not in')

# 値が入っていない場合
# false→0 '' [] {} () set()
is_ok =True
if is_ok:
    print('ok!')
else:
    print('ok!')    

is_empty = None
if is_empty is not None:
    print("None!")


#while else文
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

#input文
#while True:
#    word = input('Enter: ')
#    if word == 'ok':
#        break
#    print('next')

#for文
l = [1,2,3,4,5]
for i in l:
    print(i)

#for else文
l = [1,2,3,4,5]
for i in l:
    print(i)
else:
    print('done!')

#range
for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10,3):
    print(i)

for _ in range(10):
    print('hello')

#enumerate インデックスが欲しい時
for i, fruit in enumerate(['apple','banana']):
    print(i,fruit)

#zip 辞書型を作りたいとき
hoges =['a','b','b']
foos =[1,2,3]
for hoge,foo in zip(hoges,foos):
    print(hoge,foo)

#dict型のfor
d = {'x':100,'y':200}
for k, v in d.items():
    print(k,':',v)


#keyword argment
def menu(entree,drink,dessert):
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef',drink='drink',dessert='dessert')

#デフォルト引数で気を付けること
def test_func(x, l=[]):
    l.append(x)
    return l
r = test_func(100)
print(r)

r = test_func(100)
print(r)
# 参照渡しのもの、リストやdictをデフォルト引数にしちゃダメ！


def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
r = test_func2(100)
print(r)

r = test_func2(100)
print(r)

#引数のタプル化
def say_something(*args):
    print(args)
    for arg in args:
        print(arg)
    print('')
say_something('Hi','Mike','Nance')

def say_something2(word,*args):
    print(word)
    for arg in args:
        print(arg)
say_something2('Hi','Mike','Nance')

t = ('tuple','tuple2')
say_something2('Hi',*t)

#引数の辞書化
def menu2(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

menu2(entree='beef',drink='coffee',drink2='coffee2')
d = {'entree':'beef','drink':'coffee'}
menu2(**d)

#Docstring
def docstring():
    """
    hohohohohohoho
    """
print(docstring.__doc__)

#クロージャ
#関数の設定だけして実行しない
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

#デコレータ
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:',func.__name__)
        print('args:',args)
        print('kwargs:',kwargs)
        result = func(*args, **kwargs)
        print('result:',result)
        return result
    return wrapper

@print_more
def add_num(a,b):
    return a + b

@print_more
def sub_num(a,b):
    return a - b


print(add_num(10,20))
print(sub_num(10,20))


#ラムダ
test = ['Aaa','bbb']
def change_words(words, func):
    for word in words:
        print(func(word))

change_words(test,lambda word: word.capitalize())

# ジェネレータ
def greeting():
    yield 1
    yield 2
    yield 3

for g in greeting():
    print(g)

print('#####################3')
g = greeting()
print(next(g))
print(next(g))
print(next(g))

#リスト内包表記
t = (1,2,3,4,5)
r = [i for i in t]
print(r)

r = [i for i in t if i % 2 == 0 ]
print(r)

#辞書内包表記
w = [1,2,3]
f = ['a','b','c']

d = {}

for x, y in zip(w,f):
    d[x] = y

print(d)

d = {x:y for x,y in zip(w,f)}
print(d)

#集合内包表記
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

#ジェネレータ内包表記
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

t = tuple(i for i in range(10))
print(type(t))
print(t)


#名前空間とスコープ
animal = 'cat'
def aaa():
    #print(animal) エラーになる
    animal = 'dog'
    print('local:',locals())

aaa()
print('global:', globals())


#エラーハンドリング
l = [1,2,3]
i = 5

try:
    l[i]
except IndexError as exc:
    print("Don't worry: {}".format(exc))
else:
    print("success")
finally:
    print('clean up')
print("last")


#独自例外
class UppercaseError(Exception):
    pass

def check():
    words = ['A','b','c']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault, Go next : {}'.format(exc))
