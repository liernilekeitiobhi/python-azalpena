
# ZERRENDAK


Aldagai bat baino gehiago aldagai bakarrean gordetzea ahalbidetzen digute `[...]` artean eta `,`-ekin bananduta idazten baditugu. 
```text
zerrenda = [aldagaia_1, aldagaia_2, ...]
```

Edozein aldagai mota gorde dezakegu zerrendan.
```python title=""
zerrenda = [2.34, 'Kaixo', True] # Kasu honetan: Float, String, Boolean
```

!!! tip "TEORIA: zerrendak"
    ```text
    zerrenda = [aldagaia_1, aldagaia_2, aldagaia_3]
    ```
    Zerrenda batean elementu bakoitzak posizio bat hartzen du. Goiko zerrendan:

    - `aldagaia_1` 0.posizioan dago
    - `aldagaia_2` 1.posizioan dago
    - `aldagaia_3` 2.posizioan dago

## :arrow_right: ZERRENDEN SORRERA
<hr>
Zerrenda bat hainbat modutare sor daiteke. 

##### (i) Zerrenda hutsik hasi eta gero betetzen joan
```python title=""
zerrenda = []
# Kodean zehar behar dugunarekin beteko dugu
# Momentuz hutsik dago:
print(zerrenda)
```

##### (ii) Zerrenda hasieratik bete
```python title=""
zerrenda = ['gorria', 'berdea', 'urdina']
print(zerrenda)
```

Luzea bada, lerro ezberdinetan jarri dezakegu identazioa errespetatuz.
```python title=""
zerrenda = ['gorria',
            'berdea',
            'urdina',
            'horia',
            'morea',
            'beltza',
            'txuria',
           ]
print(zerrenda)
```
##### (iii) `list()` funtzioa erabili
```python title=""
zerrenda = list(('gorria','berdea', 'urdina')) # Kontuz, parentesi bikoitza!
print(zerrenda)
```

##### (iv) Testu bat zatitu `split()` metodoa erabiliz
```python title=""
testua = 'Euskara Euskal Herriko hizkuntza da. Hizkuntza bakartua da, ez baitzaio ahaidetasunik aurkitu. Euskaraz mintzo direnei euskaldun deritze.'
zerrenda = testua.split() # Split hutsik utziz gero, espaziotatik sortuko du zerrenda
print(zerrenda)
print('----------------------------------')
zerrenda = testua.split('.') # Split funtzioan sartutako argumentutik sortuko du zerrenda
print(zerrenda)
```

## :arrow_right: ZERRENDAREN LUZEERA
<hr>

`len()` funtzioak zerrendan dauden elementu kopurua esango digu.

```python title="zerrenda_luzeera.py"
zerrenda = ['gorria', 'berdea', 'urdina']
luzeera = len(zerrenda)
print(luzeera)
```

## :arrow_right: ZERRENDAKO ELEMENTUAK AUKERATZEN
<hr>

`string` baten antzera funtzionatzen du, posizio horretan dagoen elementua osorik hartuz.

```python title="zerrendako_elementuak_posizioka.py"
zerrenda = ['gorria', 'berdea', 'urdina']
print('0.posizioan: ',zerrenda[0])
print('1.posizioan: ',zerrenda[1])
print('2.posizioan: ',zerrenda[2])
```

:warning: Kontuz, ez eskatu zerrendatik kanpo dagoen indize bat!
```python title="errorea.py"
zerrenda = ['gorria', 'berdea', 'urdina']
print('3.posizioan: ',zerrenda[3]) # 'list index out of range' errorea emango digu, ez baita 3.posizioa existitzen.
```

Batzuetan ez dugu zerrendaren luzeera jakingo. Eta `len()` funtzioa erabili beharko dugu. Kontuz honekin, posizioak 0tik hasten direnez, zerrendako azken elementua ez da luzeeraren berdina izango, baizik eta bat gutxiago. 

```python title="luzeera_posizioa_zehazteko.py"
zerrenda = ['gorria', 'berdea', 'urdina']
luzeera = len(zerrenda)
print('Elementu kopurua: ', luzeera)
print('Azken posizioa: ', luzeera-1)
print('Azken posizioko elementua: ',zerrenda[luzeera-1]) 
print('Azken posizioko elementua-beste modu bat: ',zerrenda[-1]) 
```
```python title="errorea.py"
zerrenda = ['gorria', 'berdea', 'urdina']
luzeera = len(zerrenda)
print('Azken posizioan: ',zerrenda[luzeera]) # list index out of range errorea emango digu
```

Stringetan bezala zati bat aukeratu dezakegu:

```python title="azpizerrenda.py"
zerrenda = ['gorria', 'berdea', 'urdina', 'horia', 'morea']
print('Azpizerrenda 1.posiziotik 3.nera: ')
print(zerrenda[1:4]) # Gogoratu 4.posiziokoa ez dela sartzen
```

Zerrendak berak `<list>` mota izango du, baina elementu bakoitzak berea.
```python title="errorea.py"
zerrenda = ['gorria', 2, True]
print(type(zerrenda))
print(type(zerrenda[0])) 
print(type(zerrenda[1])) 
print(type(zerrenda[2]))  
```
## :arrow_right: ELEMENTU BAT ZERRENDAN DAGO?
<hr>

```python title="in.py"
zerrenda = ['gorria','berdea', 'urdina']
print('gorria' in zerrenda)
print('berd' in zerrenda) # Elementua osorik hartzen du kontuan
```

```python title="not_in.py"
zerrenda = ['gorria','berdea', 'urdina']
print('gorria' not in zerrenda)
print('morea' not in zerrenda) 
```

## :arrow_right: ZERRENDAKO ELEMENTUAK ALDATU
<hr>

Zerrendak oso moldagarriak dira. Elementuak aldatzea, berriak sartzea, ezabatzea... oso erraza da. 

```python title="elementua_aldatu.py"
zerrenda = ['gorria','berdea', 'urdina']
# 0.Posizioan beste zerbait nahi dugu:
zerrenda[0] = 'morea' # gorriaren ordez morea jarri
print(zerrenda)
```

Zati bat baino gehiago ere aldatu dezakegu:

```python title="azpizerrenda_aldatu.py"
zerrenda = ['gorria','berdea', 'urdina', 'horia', 'arroxa']
# 1.Posiziotik 2.nera beste zerbait nahi dugu (berdea eta urdinaren ordez beste bi):
zerrenda[1:3] = ['morea','txuria'] 
print(zerrenda)
```



## :arrow_right: ELEMENTU BERRI BAT SORTU
<hr>
Zerrendak nahi bezain beste luzatu ditzakegu (ordenagailuko memoriak puf :boom: egiten duen arte behintzat). Elementu asko badira, eskuz banan-banan sartzea ez da praktikoa, horregatik zerrendetan kode bidez elementuak nola sartu ikasi behar da. 

Ohikoena zerrendaren amaieran elementu berri bat sartzea da `append()` metodoaren bidez. `gure_zerrenda.append(gehitu_nahi_duguna)` formatuan erabitzen da.

```python title="append.py"
zerrenda = ["gorria", "berdea", "urdina"]
zerrenda.append("morea") # azken posizioan sartuko da
print(zerrenda)
```


`insert()` metodoa erabili dezakegu, posizio jakin batean elementu bat sartzeko.
Formatua: `gure_zerrenda.insert(posizioa,elementua)`
```python title="insert.py"
zerrenda = ["gorria", "berdea", "urdina"]
zerrenda.insert(2, "marroia") # "marroia" 2.posizioan sartuko da
print(zerrenda)
```

## ZERRENDATIK ELEMENTUAK EZABATU
<hr>

`remove()` metodoak esaten diogun elementu bat (bakarra) ezabatuko du.

```python title="remove.py"
zerrenda = ['gorria', 'urdina','horia','beltza','urdina']
zerrenda.remove('urdina') # Aurkitzen duen lehena ezabatuko du soilik
print(zerrenda)
```

`pop()` metodoak esaten diogun indizeko elementua ezabatuko du.
```python title="pop.py"
zerrenda = ['gorria', 'urdina','horia','beltza','urdina']
zerrenda.pop(1) # 1.posizioko elementua ezabatuko du
print(zerrenda)
```

```python title="pop_argumentu_gabe.py"
zerrenda = ['gorria', 'urdina','horia','beltza','urdina']
zerrenda.pop() # Ez badiogu indizea zehazten azken elementua kenduko du
print(zerrenda)
```

`del` hitz bereziak esaten diogun indizeko elementua ezabatuko du.
```python title="del_indizea.py"
zerrenda = ['gorria', 'urdina','horia','beltza','urdina']
del zerrenda[1] # 1.posizioko elementua ezabatuko du
print(zerrenda)
```

```python title="del_osorik.py"
zerrenda = ['gorria', 'urdina','horia','beltza','urdina']
del zerrenda # Zerrenda guztia ere ezabatu dezakegu
print(zerrenda) # Errorea emango du, ez baitago zerrendarik
```


## :arrow_right: ZERRENDAK ELKARTU
<hr>
Batzuetan bi zerrenda edukiko ditugu eta zerrenda bakarra sortu nahi izango dugu.

Aukera bat `+` sinboloa erabiltzea da. Baina kontuz ordenarekin:
```python title="+.py"
zerrenda_1 = ["gorria", "berdea", "urdina"]
zerrenda_2 = ["2", "3", "4"]
zerrenda_elkartuta = zerrenda_1 + zerrenda_2
print (zerrenda_elkartuta)
zerrenda_elkartuta_alderantziz = zerrenda_2 + zerrenda_1
print (zerrenda_elkartuta_alderantziz)
```

`extend()` metodoa ere erabili daiteke. Kasu honetan ordea, ez da aldagai berri bat sortzen, baizik eta dugun bat aldatzen dugu. Formatua:
 `aldagaia.extend(gehitu_nahi_dugun_zerrenda)`

Adibide honetan, `zerrenda_1` aldagaiari aplikatuko diogu metodoa. Beraz, hau 'in-place' aldatuko da. Hau da, zerrenda originala eraldatuko dugu.
```python title="extend.py"
zerrenda_1 = ["gorria", "berdea", "urdina"]
zerrenda_1.extend(["2", "3", "4"]) # zerrenda_1 aldagaiari aplikatzen diogu metodoa
print (zerrenda_1) #zerrenda_1 originala jada ez daukagu
```

## :arrow_right: ZERRENDAK ORDENATU
<hr>

`sorted()` funtzioa edo `sort()` metodoa erabili dezakegu. Funtzioak kopia berri bat sortuko digu aldagai batean gorde dezakeguna, metodoak berriz zerrenda *in-place* aldatuko du.


```python title="sorted()_funtzioa.py"
zerrenda = [5,0,7,2,9,1]
zerrenda_ordenatua = sorted(zerrenda) # Funtzioak zerrenda ordenatu du eta kopia bat eman digu guk aldagai batean gorde dezakeguna
print('Zerrenda ordenatua: ',zerrenda_ordenatua) 
print('Zerrenda originala: ',zerrenda) # Zerrenda originala berdin mantentzen da
```

```python title="sort()_metodoa.py"
zerrenda = [5,0,7,2,9,1]
zerrenda.sort()
print('Zerrenda: ',zerrenda) # Metodoa aplikatzeak zerrenda originala aldatu du
```

Metodoa erabiliz zerrenda originala gorde nahi badugu, aldagai auxiliar bat erabili behar da.

```python title="originala_gorde_gaizki.py"
zerrenda = [5,0,7,2,9,1]
zerrenda_aux = zerrenda
zerrenda.sort() # Zerrenda originala ordenatzen dugu hemen
print(zerrenda) # Zerrenda originala galdu dugu
print(zerrenda_aux) # Zerrenda auxiliarra ere aldatu da
```

`zerrenda_aux = zerrenda` egitean, bi aldagaiek erreferentzia bera dute (objektu berera apuntatzen ari dira. Ikusi: ["Non daude aldagaiak kodea exekutatzen den bitartean?"](aldagai-motak.md#arrow_right-non-daude-aldagaiak-kodea-exekutatzen-den-bitartean) atala). Horregatik, `sort()` aplikatzean biak aldatzen dira (in-place delako).

Hainbat modu daude originala gordetzeko:
```python title="originala_gorde_ondo.py"
zerrenda = [5,0,7,2,9,1]
zerrenda_kopia_1 = zerrenda.copy() # Kopia independente bat sortzen duen metodoa
zerrenda_kopia_2 = list(zerrenda)
zerrenda_kopia_3 = zerrenda[:]
zerrenda.sort() # zerrenda originala ordenatu dugu, baina gainontzekoak kopia independenteak dira
print(zerrenda)
print('k1: ',zerrenda_kopia_1) 
print('k2: ',zerrenda_kopia_2) 
print('k3: ',zerrenda_kopia_3)
```
## :arrow_right: ZERRENDEN ZERRENDAK

Interesgarria da zerrenden barruan zerrendak gorde ditzakegula. Adibidez:

```text title="zerrenden_zerrendak.py"
ikasleen_nota = [['Ane',8],['Jon',6.3],['Maider',9.6],['Aitor',3]]
```

Kasu honetan, zerrenda handiaren elementu bakoitza beste zerrenda bat da, ikaslearen izena eta nota gordetzen dituena. Horrelakoetarako ordea, egokiagoa da [hiztegiak](hiztegiak.md) erabiltzea.

Horren ordez, sor dezagun 3x3 dimentsioko matrize bat:
```text title="zerrenden_zerrendak_matrizea.py"
matrizea = [[2,-3,1],[7,5,-1],[0,12,4]]
```
Zerrenda honek 3 elementu ditu eta hauetako bakoitza 3 elementuko beste zerrenda bat da. Matrizea deitu diezaiokegu horrela adieraziz gero:
```sh
   2  -3  1      # 1.LERROA: zerrenda handiko 0.elementua
   7  5  -1      # 2.LERROA: zerrenda handiko 1.elementua
   0  12  4      # 3.LERROA: zerrenda handiko 2.elementua
```

Nola aukeratu elementuak? Kortxete bikoitzarekin: lehen kortxetean zerrenda handiko posizioa zehaztuko dugu eta bigarrenean posizio horretan dagoen zerrenda txikiko hartu nahi dugun elementuaren posizioa.

```python title="zerrenden_zerrendak_indizeak.py"
zerrenda = [['0-0','0-1','0-2'],['1-0','1-1','1-2'],['2-0','2-1','2-2']]
print('Zerrenda handiko 1.posizioan eta bertan dagoen zerrenda txikiko 2.posizioan elementu hau dago:')
print(zerrenda[1][2])
print('Zerrenda handiko 2.posizioan zerrenda hau dago:')
print(zerrenda[2])

```

Goiko matrizera itzuliz:
```python title="matrizeen_indizeak.py"
matrizea = [[2,-3,1],[7,5,-1],[0,12,4]]
lerr2_zut1 = matrizea[1][0] 
print('2.lerroko 1.zutabeko elementua: ',lerr2_zut1)
```


## :arrow_right: AUKERA GEHIAGO

Gainontzeko aldagai moten moduan zerrendek ere metodo gehiago dituzte:
[https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

