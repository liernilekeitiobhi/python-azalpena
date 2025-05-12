# ZENBAKIAK


!!! tip "ZENBAKI MOTAK"
    Hiru zenbaki mota:

    - Osoak (Integer): 1; 2; 3466; -253; ...
    - Hamartarrak (Float): 1.26; 2.00; 4.0000000000; ....
    - Konplexuak (Ez dira ia erabiltzen)

Garrantzitsua izango da jakitea zein zenbaki mota dugun aldiro, bestela zaila izango da kodean zehar errorea detektatzea.


## :arrow_right: ERAGIKETAK
<hr>
!!! tip "TEORIA: Eragiketak zenbakiekin"
    - `+`, `-`, `*`, `/`: plus, minus, bider eta zati
    - `**`: berreketa
    - `//`: zatiketaren zati osoa
    - `%`: zatiketaren hondarra

```python title="zatiketan_float.py"

# Nahiz eta zatiketa bat zehatza izan, beti Float lortuko dugu.
x = 8
y = 2
print('Zatiketaren emaitza: ', x/y)
print('Zatiketaren emaitzaren mota: ', type(x/y))
```

```python title="zatiketa_motak.py"
x = 10
y = 3
print(x,'/',y, 'emaitza: ', x/y, '| Mota: ',type(x/y))
print(x,'/',y, 'ren zati osoa: ', x//y, '| Mota: ',type(x//y))
print(x,'/',y, 'ren hondarra: ', x%y, '| Mota: ',type(x%y))
```

## :arrow_right: TYPE ALDAKETAK
<hr>

```python title="type_aldaketak_1.py"
x = 4.0
print(type(x)) # Hemen x float da
x = int(x) # x int izatera aldatu
print('x berria: ',x)
print(type(x))
```

```python title="type_aldaketak_2.py"
x = 6
print(type(x)) # Hemen x int da
x = float(x) # x float izatera aldatu
print('x berria: ',x)
print(type(x))
```

## :arrow_right: AUKERA GEHIAGO
<hr>
Pythonek mila eta mila aukera ematen dizkigu zenbakiekin aritzeko. Apurka-apurka deskubritzen joan behar gara sortzen zaizkigun beharren arabera.:mag: 

Hemen adibidetxo bat `math` [modulua](moduluak-lib-pak.md) erabilita. Moduluak jada sortuta dauden kode zatiak dira, eta bertatik funtzioak, aldagaiak... har ditzakegu. Modulu bakoitzak bere dokumentazioa du. Adibidez, `math` moduluarena: [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)
```python title="math_modulua_erabiltzen.py"
import math # modulua inportatu behar dugu erabili ahal izateko
pi_zenbakia = math.pi # math modulutik pi hartzen dugu
print(pi_zenbakia)
# Pi zenbakia bi dezimalekin soilik:
print(round(pi_zenbakia,2))
```

## :arrow_right: JARRI PRAKTIKAN
<hr>

##### 1.ARIKETA

Izendatu bi aldagai. `x=11`eta  `y=3`. 

- Inprimatu x/y-en emaitza 2 dezimalekin.
- Inprimatu x/y egitean sortzen den hondarra.
- Inprimatu marra horizontal bikoitz bat.
- `eragiketa` izeneko aldagai batean gorde: x/y-ren_emaitza_osoa * y + lehen_kalkulatutako_hondarra
- Kodearen amaieran kopiatu hau: `print(eragiketa, '=', x)`
- Exekutatu kodea


Esperotako emaitza ZEHATZ-MEHATZ:
```sh
11 / 3 egitean 3.67 lortzen da.
11 / 3 egitean sortzen den hondarra:  2
========================================
11 = 11
```

##### 2.ARIKETA

- Inportatu `random` modulua
- Gorde aldagai batean 1 eta 20 tarteko ausazko zenbaki oso bat (dokumentazioa begiratu nola egiten den ikusteko).
- Inprimatu aldagaia eta ikusi nola kodea exekutatzen den bakoitzean zenbaki ezberdin bat inprimatzen den. 