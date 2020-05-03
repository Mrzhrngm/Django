d = {'Michael':95, 'Bob':75, 'Lucy':89}
print(d)
print(d['Michael'])
print(d['Bob'])
d['aa']=3
print(d['aa'])
d['Jack'] = 90
print('d[\'Jack\'] is %s' % d['Jack'])
d['Jack'] = 39
print('d[\'Jack\'] is %s' % d['Jack'])
print('hh' in d)
print(d.get('jack',-1))
print('d[\'Jack\'] is %s' % d.get('Jack',-1))
#help(abs)
print(abs(-19))
n1=299
print(hex(n1))
from abstest import my_abs
print (my_abs(-8))
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('aa', 'asd', '7', 'beijing')
enroll('xx','89')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(3,5,6,9))

pip