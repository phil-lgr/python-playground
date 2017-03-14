# dictionnary
# keys can be number or string
age = 'age'
dic = {
    'name': 'phil',
    'last': 'leger',
    age: 12,
    1: 23,
    1: 24
}
print dic
print dic[1]
print dic['name']
print [v for v in (dic.keys())]
print dic.items()
# empty
dic2 = {}
dic2['age'] = 12
dic2['dic'] = {'dic2': 2}
print dic2