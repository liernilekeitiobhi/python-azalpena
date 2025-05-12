# STRING

`'...'` edo `"..."` artean adierazten dena Pythonek string (testu) bat moduan hartzen du. Oso erabilgarria da testu luzeak prozesatzeko, bilaketak egiteko, ordenatzeko...

## :arrow_right: TESTUA ALDAGAI MODUAN
<hr>

```python title="testua_aldagai_batean.py"
esaldia = 'Kaixo, mundua'
print(esaldia)
```

Zenbakiekin moduan `type()` funtzioak gure aldagaiaren mota esango digu, kasu honetan `str`.
```python title="type_str.py"
esaldia = 'Kaixo, mundua'
print(type(esaldia))
```

!!! warning "ZENBAKIAK TESTU IZAN DAITEZKE"
    `'...'` edo `"..."` artean zenbaki bat badago, Pythonentzat string bat da.

## :arrow_right: TESTUA ERALDATZEN
<hr>

Testuaren karaktere bakoitzak 0-tik hasita, zenbakizko posizio bat hartzen du. Hori jakinda, testua eraldatu dezakegu: karaktereak hartu, zatiak isolatu...

!!! tip "TEORIA: Testua eraldatzen"
    - Bi testu konkatenatu: `+`
    - Hurrengo lerrora pasatu: `\n`
    - n.posizioko karakterea hartu: `aldagia[n]`
    - Eskuinetik hasita n.posizioko karakterea hartu: `aldagia[-n]`
    - Testuaren zati bat hartu (a poisziotik b-1 posiziora): `aldagia[a:b]` :warning: `b` ez da sartzen!
    - Hasieratik a-1 posiziora:`aldagia[0:a]` edo `aldagia[:a]` :warning: `a` ez da sartzen!
    - b posiziotik amaierara: `aldagia[b:]`
    - Testuaren karaktere kopurua jakin: `len(aldagaia)`

```python title="testua_konkatenatu.py"
lehen_aldagaia = 'Kai'
bigarren_aldagaia = 'xo, mundua'
print(lehen_aldagaia + bigarren_aldagaia)
```

:warning: Kontuz zenbakiekin!

```python title="zenbakia_edo_str.py"
lehen_aldagaia = 2
bigarren_aldagaia = 5
print('Zenbakien batura: ',lehen_aldagaia + bigarren_aldagaia)
lehen_aldagaia = '2'
bigarren_aldagaia = '5'
print('String konkatenazioa: ',lehen_aldagaia + bigarren_aldagaia)

```

Eraldaketak ulertzeko ezinbestekoa da norberak frogak egitea!
```python title="eraldaketa_batzuk.py"
esaldia = 'Kaixo, mundua'
print('Esaldiaren karaktere kopurua: ', len(esaldia))
print('Esaldiaren 0.posizioko karakterea: ', esaldia[0])
print('Esaldiaren 5.posizioko karakterea: ', esaldia[5])
print('Esaldiaren 2.posiziotik 7.nera: ', esaldia[2:8]) # 8.na ez da sartzen
print('Esaldiaren azken karakterea, 1.modua: ', esaldia[-1])
print('Esaldiaren azken karakterea, 2.modua: ', esaldia[len(esaldia)-1])

```

## :arrow_right: AUKERA GEHIAGO
<hr>

Zenbakiekin moduan, testuarekin ere askoz ere aukera gehiago daude, hauek eraldatzeko, bilaketak egiteko, idazteko, ezabatzeko...

Link honetan `string` motako aldagai bati aplikatu daitezkeen *built-in* metodoak daude: [ https://www.w3schools.com/PYTHON/python_strings_methods.asp]( https://www.w3schools.com/PYTHON/python_strings_methods.asp)

Adibidez:
```python title="metodo_batzuk.py"
esaldia = '   Kaixo, mundua, kaixo'

esaldia_maiuskulaz = esaldia.upper()
esaldia_minuskulaz = esaldia.lower()
esaldia_hitza_aldatuta = esaldia.replace('Kaixo', 'Hello')
esaldia_ertzetako_espazioak_kenduta = esaldia.strip()
print(esaldia_maiuskulaz)
print(esaldia_minuskulaz)
print(esaldia_hitza_aldatuta)
print(esaldia_ertzetako_espazioak_kenduta)

```

## :arrow_right: JARRI PRAKTIKAN
<hr>

