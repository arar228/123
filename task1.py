#CREATE

a = 'привет' 
b = "привет" 
c = "я 'знаю' Python" 

d = 'я "знаю" Python' 
e = 'я "знаю' Python" 

a = 123
a = str(a) 
str([1, 1.1, 'a']) 
str(True) 
str(None) 

a = 'привет'
b = 'Иван'

c = f"{a} я {b}" 

#READ

a = 'привет'
print(a)
print('Иван')

a = 'привет'
a[0] 
a[1] 
a[2] 
a[3] 
a[4] 
a[5]
a[6] 
a[-1] 
a[-2] 
a[-3] 
a[-4] 
a[-5] 
a[-6] 
a[-7] 

#UPDATE

a = 'привет'
a[0] = 'б' 
a = 'бривет'

#DELETE

a = 'привет'
del a[0] 
del a 

a = 'привет'
b = 'Мир'
c = f"{a} и {b}"
print(c) 
c += b 

a = 'привет'
b = 2
c = a * b
print(c) 
a *= b 

a = " 
b = "" 
c = str()

help(str) 
a = 'привет мир'
a.count('p') 
a.find('вет') 
a.index('вет') 
a.rfind('p') 
a.rindex('p')

a = 'привет Мир'
a.removeprefix('пр') 
a.removesuffix('ир') 
a.replace('p', 'P', 1) 
a.capitalize()
a.lower() 
a.upper() 
a.swapcase() 


S = 'Кит на море не романтик'
S.spit()
[ 'Кит' 'на' 'море' 'не' 'романтик' ]
str.lower(S)
S.lower()

a = '1,2,3,4'
print(a, sep="-")
1_2_3_4
