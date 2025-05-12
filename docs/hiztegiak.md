# HIZTEGIAK

Aurreko atalean zerrendaz osaturiko zerrenda hau sortu dugu:
```text
ikasleen_notak = [['Ane',8],['Jon',6.3],['Maider',9.6],['Aitor',3]]
```

Baina Pythonek badu objektu bat horrelakoak erraztasunez kudeatzeko: hiztegiak. 

## :arrow_right: HIZTEGIA ULERTZEN
<hr>

Hiztegia hitz gako bat balio batekin erlazionatzen duen objektu mota da. Horrelakoa da bere sintaxia:

```python title="hiztegi_adibidea.py"
ikasleen_notak = {'Ane':8,'Jon':6.3,'Maider':9.6,'Aitor':3}
```

Oso luzea bada hainbat lerrotan idatzi dezakegu identazioa errespetatuz:
```python title="hiztegi_adibidea_2.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print(ikasleen_notak)
```

Hiztegiko elementu bakoitzak bi atal ditu: giltza(*key*) eta balioa(*value*). Edozein modutara ordena dezakegu, hau da, elementuek ez dute indize jakin bat `list` eta `string`etan moduan.

0.posizioan dagoen elementua inprimatzen saiatzen bagara, zerrendetan bezala, errorea emango digu:

```python title="hiztegiko_elementuak_errorea.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print(ikasleen_notak[0])
```

Horren ordez, balioak giltzaren bitartez atera beharko ditugu:
```python title="hiztegiko_elementuak_giltza_bidez.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print('Anek atera duen nota:')
print(ikasleen_notak['Ane'])
```

Horregatik, oso garrantzitsua da giltzen izenak ez errepikatzea. Bakarrak izan behar dira, bestela Pythonek ez du jakingo errepikatutako giltzen artean zeinen balioa atera behar duen. Balioak arazo gabe errepikatu daitezke ordea: bi ikaslek nota berdina atera badute, ez dago arazorik. 

!!! tip "TEORIA: Hiztegiak"
    Hiztegiak **giltza** bat **balio** batekin lotzen duen objektuak dira. 
    Giltzak bakarrak izan behar dira (ezin dira errepikatu), baina balioak guk nahi dugun modukoak eta motatakoak izan daitezke. Adibidez:
    ```python title=""
    hiztegi_adibidea = {'giltza_1': [1,2,3], # Balioa zerrenda da
                        'giltza_2': 'kaixo', # Balioa str da
                        'giltza_3': 4.5      # Balioa float da
                       }
    ```


## :arrow_right: HIZTEGIEN SORRERA
<hr>
Zerrendetan moduan hiztegi huts bat sor dezakegu eta kodean zehar betetzen joan:
```python title="hiztegi_hutsa_1.py"
hiztegia = {}
# Gero beteko dugu
```

```python title="hiztegi_hutsa_2.py"
hiztegia = dict()
# Gero beteko dugu
```

Hasieratik balioak ematea ere beste modu bat da, ikasleen_notak aldagaiean egin dugun moduan.

Zerrenda batetik abiatuz ere sor daiteke `dict()` funtzioari argumentutzat zerrenda sartuz:
```python title="hiztegia_zerrendatik.py"
hiztegia = dict([['Ane',8],['Jon',6.3],['Maider',9.6],['Aitor',3]])
print(hiztegia)
```

Modu gehiago ere badaude. Momentuan komeni zaigunaren arabera moldatu behar gara beti.

## :arrow_right: HIZTEGIKO ELEMENTU KOPURUA
<hr>

Beti bezala, `len()` erabili dezakegu, eta elementu kopurua emango digu. Baina gogoratu hiztegiko elementu bakoitzak bi atal dituela. 

```python title="hiztegia_elementuak.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print(len(ikasleen_notak))
```

Nahiz eta balioak konplikatu, lau giltza badaude lau elementu egongo dira:
```python title="hiztegia_elementuak.py"
# Balioak tuplez osatutako hiztegiak dira kasu honetan.
ikasleen_notak = {'Ane':[('1.ebal',8), ('2.ebal',8), ('3.ebal',8)],
                  'Jon':[('1.ebal',5.6), ('2.ebal',7.4), ('3.ebal',7.5)],
                  'Maider':[('1.ebal',9.5), ('2.ebal',10), ('3.ebal',8.3)],
                  'Aitor':[('1.ebal',4), ('2.ebal',5), ('3.ebal',3)],
                 }
print(len(ikasleen_notak))
```



## :arrow_right: HIZTEGIEN ELEMENTUETARA AKZEDITZEN
<hr>

##### BALIOETARA
Giltza konkretu baten balioa nahi izanez gero, errazena giltzaren izena erabiltzea da:
```python title="hiztegiko_balioak_giltza_bidez.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print(ikasleen_notak['Ane']) # Aneren balioa:8
```

Balio guztiak nahi izanez gero, bakoitza norena den inporta gabe:
```python title="hiztegiko_balio_guztiak.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
balio_guztiak = ikasleen_notak.values()
print(balio_guztiak, '|MOTA: ', type(balio_guztiak)) 
# KONTUZ! badirudi zerrenda bat dela, baina ez da.
# values() metodoak dict_values objektu berezi bat itzulzen du,
# eta hauek ezin dira aldatu edo indexatu zerrenda bat bezala.
# Askotan zerrenda bat edukitzea komodoagoa denez:
balio_guztien_zerrenda = list(balio_guztiak)
print('Zerrendara bihurtuta: ', balio_guztien_zerrenda)
```


##### GILTZETARA
```python title="hiztegiko_giltzak.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
giltzak = ikasleen_notak.keys() # Zerrenda bat dirudi, baina ez da!
print(giltzak)
# Lehengo moduan, zerrenda nahi badugu:
print(list(giltzak))
```


##### BIAK BATERA
```python title="biak_batera.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
giltza_eta_balioa = ikasleen_notak.items() # Zerrenda bat dirudi, baina ez da!
print(giltza_eta_balioa)
# Lehengo moduan, zerrenda nahi badugu:
print(list(giltza_eta_balioa)) # Tuplak zerrenden barnean
```

## :arrow_right: ELEMENTU BAT BADAGO HIZTEGIAN?
<hr>

##### GILTZA
Giltza hiztegien oinarria izanik `giltza in hiztegia` galdetzea nahikoa da. 
```python title="giltza_badago.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print('Jon' in ikasleen_notak)
print('Mikel' in ikasleen_notak)
```

##### BALIOA
Balioetarako berriz, `balioa in hiztegia.values()` egin beharko dugu. 
```python title="balioa_badago.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
print(8 in ikasleen_notak.values())
print(0 in ikasleen_notak.values())
```

## :arrow_right: HIZTEGIKO ELEMENTUAK ALDATU
<hr>

Giltza baten balioa aldatzea erraza da, akzeso zuzena baitugu balio horretara giltzaren izena jakinda.
```python title="balioa_aldatu.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak['Ane'] = 4 # Aneri 4 jarri diogu 8 ordez
print(ikasleen_notak)
```

`update()` metodoak berdina egingo du:
```python title="balioa_aldatu.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak.update({'Ane':4}) # Aneri 4 jarri diogu 8 ordez
print(ikasleen_notak)
```

Balioak aldatzerako orduan, originala kontuan hartzea posible da. Adibidez, Aitorri puntu 1 igo nahi diogu jarrera ona edukitzeagatik:

```python title="balioa_eraldatu.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak['Aitor'] = ikasleen_notak['Aitor'] + 1 # Oraingoa = Lehengoa + 1
print(ikasleen_notak)
```

Balio konkretu bati dagokion giltza aldatzea ordea ez da erraza. Hasteko ez dakizu balio hori behin baino gehiagotan errepikatuta ote dagoen, beraz, ez duzu jakingo giltza egokia aldatzen ari ote zaren. Jakinda ere ez dago metodo zuzen bat balioa jakinda giltzara akzeditzeko. Errazena nahi duzun giltza ezabatu, eta berria sortzea da. 




## :arrow_right: ELEMENTU BERRIAK SORTU
<hr>

Giltza eta balio berri bat definitzea nahikoa da. 

```python title="balioa_eraldatu.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak['Julen'] = 8.6 # Julen gehitzen dugu hiztegira 8.6 notarekin
print(ikasleen_notak)
```

## :arrow_right: ELEMENTUAK EZABATU
<hr>

Gogoratu elementuaren dei nagusia giltza bidez egiten dugula. Beraz, elementua ezabatzeko giltzari deituko diogu. Honek bere balioa ere ezabatuko du:

```python title="pop.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak.pop('Jon') # Jon giltza eta balioa ezabatu
print(ikasleen_notak)
```

Beste modu bat:

```python title="del.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
del ikasleen_notak['Jon'] # Jon giltza eta balioa ezabatu
print(ikasleen_notak)
```

Hiztegia osorik ere ezabatu dezakegu:
```python title="del.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
del ikasleen_notak 
print(ikasleen_notak) # Errorea emango digu, hiztegia ezabatu baitugu
```

Hiztegia hustu dezakegu:
```python title="clear.py"
ikasleen_notak = {'Ane':8,
                  'Jon':6.3,
                  'Maider':9.6,
                  'Aitor':3
                 }
ikasleen_notak.clear()
print(ikasleen_notak) # Hiztegia hutsik egongo da
```

## :arrow_right: HIZTEGIEN HIZTEGIAK
<hr>

Zerrendetan moduan, hiztegi bat beste baten barnean sar dezakegu. Bi kortxete erabiliz, balio konkretutaraino iritsi ahalko gara. 

```python title="clear.py"
ikasleen_notak = {'Ane': {'Mate':8,'Euskara':9},
                  'Jon': {'Mate':7,'Euskara':9.5},
                  'Maider': {'Mate':8.3,'Euskara':7.9},
                  'Aitor': {'Mate':4.5,'Euskara':6.3},
                 }
print('Aneren mateko nota:')
print(ikasleen_notak['Ane']['Mate']) 

print('Aneren nota guztiak:')
print(ikasleen_notak['Ane']) 

```

## :arrow_right: AUKERA GEHIAGO

Hiztegien metodo gehiago:
[https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)