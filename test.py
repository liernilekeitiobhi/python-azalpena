'''Izendatu bi aldagai. x=11, y=3. 

Inprimatu x/y-en emaitza 2 dezimalekin
Inprimatu x/y egitean sortzen den hondarra
Inprimatu marra horizontal bikoitz bat.
'eragiketa' izeneko aldagaiean gorde: x/y-ren_emaitza_osoa * y + lehen_kalkulatutako_hondarra
Kodearen amaieran idatzi: print(eragiketa, '=', x)
'''
import random
a = random.randrange(100)
print(a)
x = 11
y = 3

print(x, '/', y , 'egitean', round(x/y,2), 'lortzen da.')
print(x, '/', y , 'egitean hondarra: ', x%y)
print('====================================')
eragiketa = x//y*y+x%y
print(eragiketa, '=',x)