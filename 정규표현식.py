import re

data = '동 기업의 매출액은 전년 대비 29.2% 늘어났습니다.'
#print(re.findall('\d+.\d+%', data))


## match

p = re.compile('[a-z]+')
# print(type(p))

m = p.match('python')
#print(m.group()) # python

m = p.match('Use python')
#print(m) # None

p = re.compile('[가-힣]+')
m = p.match('파이썬')
#print(m)


## search
p = re.compile('[a-z]+')
m = p.search('python')
#print(m)

m = p.search('Use python')
#print(m)


## findall

p = re.compile('[a-zA-Z]+')
m = p.findall('Life is too short, You need Python')
#print(m)


## finditer

p = re.compile('[a-zA-Z]+')
m = p.finditer('Life is too short, You need Python')
# print(m)

#for i in m:
#    print(i)

num = """\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t15\t\t\t\r\n\t\t\t\23\r\n\t\t29\r\t\t\r34\t\t\t40"""

p = re.compile('[0-9]+')
m = p.findall(num)
#print(m)

dt = '> 오늘의 날짜는 2022.12.31 입니다.'

p = re.compile('[0-9]+.[0-9]+.[0-9]+')
m = p.findall(dt)
print(m)

p = re.compile('[0-9]+')
m = p.findall(dt)
print(''.join(m))
