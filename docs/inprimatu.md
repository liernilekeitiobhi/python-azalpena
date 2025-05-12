# NOLA JAKIN ZER ARI DEN GERTATZEN GURE KODEAN?
Aurreko atalean ikusi dugu `print()` erabiltzen ez badugu, ez daukagula ezer ikusterik. 

## INPRIMATU
<hr>
Gure kodeak ondo funtzionatzen ote duen ikusteko, momenturen batean inprimatzeko eskatu beharko diogu. Bestela ez dugu jakingo zer egin duen.

!!! tip "TEORIA: `print()` funtzioa"
    Gure kodean dagoen zerbait inprimatzeko erabiliko dugu. Kode txikietan ez da beharrezkoa, baina kodea handitzen den heinean, tartean zer gertatzen den jakiteko komenigarria izaten da. 

## ADIBIDEAK
<hr>

### :arrow_right: 1. ADIBIDEA: Zertarako `print()`
Zerbait gertatu da, baina ezin dugu zer den ikusi:
```python title="print_erabili_gabe.py"
2 + 3
```

Inprimatzen badugu, ikusiko da:
```python title="print_erabiltzen.py"
print(2+3)
```

### :arrow_right: 2. ADIBIDEA: Aldagai baten `print()`
Zerbait gertatu da, baina ezin dugu zer den ikusi:
```python title="print_erabili_gabe.py"
a = 1
b = 2
batura = a + b
```

Inprimatzen badugu, ikusiko da:
```python title="print_erabiltzen.py"
a = 1
b = 2
batura = a + b
print(batura)
```

### :arrow_right: 2. ADIBIDEA: Testua inprimatzen
Pythonek ordenean inprimatuko du beti.
```python title="testu_gabe.py"
a = 4
b = 7
batura = a + b
print(a)
print(b)
print(batura)
```

Baina kodea handitzean, ez da erraza egindako `print` guztiak identifikatzea. Horretarako oso erabilgarria da testua inprimatzea.

Testua inprimatzeko `'...'` edo `"..."` artean sartu behar da. Ondoren, aldagaiaren eta testuaren artean "koma" idatzi behar da. 
```python title="testuarekin.py"
a = 4
b = 7
batura = a + b
print('a aldagaiaren balioa: ', a)
print('b aldagaiaren balioa: ', b)
print('=====================')
print(' BIEN ARTEKO BATURA:')
print('=====================')
print(a, '+', b, '=', batura)
```

### 3. ADIBIDEA: Testua lerroz aldatzen

```python title="hurrengo_lerroa_lehen_aukera.py"
print('Lehen lerroa')
print('Bigarren lerroa')
```


Beste aukera bat ere badago. `\n` sinboloak testua hurrengo lerrora bidaliko du:

```python title="hurrengo_lerroa_bigarren_aukera.py"
print('Lehen lerroa\nBigarren lerroa')
```

## JARRI PRAKTIKAN
<hr>


Kopiatu kode hau zure ordenagailuan:

```text
a = 10
b = 4

# Zure kodea hemen joango da

```
Zure kodearekin esperotako emaitza inprimatzea lortu behar duzu. 

Esperotako emaitza hau da:

```sh
10 - 4 eragiketaren emaitza 6 da.

```



