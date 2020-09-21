#リスト型
l = [1,2,3,4,5,6]
print(l)
print(l[-1])
print(l[2:5])
print(l[::2])

#タプル型
t = (1,2,3,4,5,6)
# t[0]=0    #代入できない

num_tuple = (10,20)
print(num_tuple)

x,y = num_tuple
print(x,y)

#値の入れ替え
a = 100
b = 200

a, b = b, a
print(a,b)


#辞書型
d = {'x':10,'y':20}
print(d)
d['z'] = 200
d[1] = 2000
print(d)

print( d.keys() )
print( d.values() )
print( d.items() )


d2 = {'x':'hoge','xx':20}
d.update(d2)
print( d )

# print( d['aaa'] )　エラー
print( d.get('aaa') )

# 値のコピー
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y) #同じ値になる

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y) #違う値になる

#集合型
a = {1,2,3,4,5,5,5,5,5,6,6,6,6}
print(a)
print(type(a))
b = {2,3,3,6,7}
print(a - b)
print(a & b)
print(a | b)
print(a ^ b)


