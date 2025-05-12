# BALDINTZAK

Beti ez dugu jakingo gure kodean zer gertatzen ari den, ausazko parametro bat dugulako, datu asko prozesatzen ari garelako eta ezin dugulako guztiak nolakoak diren jakin... Horregatik baldintzazko sententziak behar ditugu. Kasu bakoitzean zer gertatzen den esango digutenak. 

## :arrow_right: `if` ULERTZEN
<hr>

Jarraian adibide sinple bat egingo dugu. `a` aldagaiari 1etik 9rako ausazko zenbaki bat esleituko diogu eta inprimatu egingo dugu zein den ikusi ahal izateko.

Ondoren, tokatu zaigun zenbakia 5 baino txikiagoa, handiagoa edo berdina ote den aztertuko dugu. Horretarako 3 if prestatuko ditugu, bakoitzak baldintza hauetako bat duelarik. Kodea goitik behera exekutatzen dela badakigu, baina `if`-etan kode zatiak salto egin ditzake baldintza betetzen ez badu. Edo berdina dena, `if` horren barrura baldintza betetzen badu soilik sartuko da. 

Zerbait `if`-aren barruan dagoela esateko, tabulazio bat eskuinerago idatzi beharko dugu. Hau da,
```text
if (baldintza):
    baldintza betetzen bada gertatzea nahi duguna
```

Exekutatu kodea behin eta berriro inprimatutako mezua nola aldatzen den ikusteko.

```python title='lehen_baldintza_adibidea.py'
import random
a = random.randrange(10) # 0etik 9rako ausazko zenbakia

print('Tokatu zaigun zenbakia: ', a)
print('BALDINTZEN ARABERA GAUZA BAT EDO BESTE INPRIMATUKO DUGU:')
if (a>5): # if honen barruan sartuko da soilik a>5 bada
    print(a, 'zenbakia 5 baino handiagoa da') # if barrukoa tabulazio 1 eskuinerago

if (a==5): # if honen barruan sartuko da soilik a==5 bada
    print('5 tokatu zaigu')

if (a<5): # if honen barruan sartuko da soilik a<5 bada
    print(a, 'zenbakia 5 baino txikiagoa da')
```

## :arrow_right: BALDINTZAZKO HITZ GEHIAGO
<hr>

Aurreko adibidearen fluxua aztertzen badugu hau da gertatzen dena:
```text
Demagun a=7 tokatu dela
if (a>5): # HAU KONPROBATUKO DU ETA SARTZEA EGOKITZEN ZAIOLA IKUSIKO DU
    print(a, 'zenbakia 5 baino handiagoa da') #HAU INPRIMATUKO DU
if (a==5): # HAU KONPROBATUKO DU ETA EZ SARTZEA EGOKITZEN ZAIOLA ERABAKIKO DU
    print('5 tokatu zaigu')
if (a<5): # HAU KONPROBATUKO DU ETA EZ SARTZEA EGOKITZEN ZAIOLA ERABAKIKO DU
    print(a, 'zenbakia 5 baino txikiagoa da')
```

Baina `if` batean sartu denean, guk badakigu besteak konprobatu beharrik ere ez dituela. Kodea handia bada eta konprobatzea asko kostatzen bazaio alperrik galdutako denbora da. 

Hau ekiditeko, `elif` existitzen da. Hitz hau `else if`-en laburdura bat da. Esan nahi duena da: aurreko `if`-ean edo `elif`-ean sartu ez bazara probatu hemen. 

```python title='elif.py'
import random
a = random.randrange(10) # 0etik 9rako ausazko zenbakia

print('Tokatu zaigun zenbakia: ', a)
if (a>5): # hemen sartzen bada ez ditu hurrengo elif-ak konprobatuko
    print(a, 'zenbakia 5 baino handiagoa da') 

elif (a==5): # hemen sartzen bada ez du hurrengo elif-a konprobatuko
    print('5 tokatu zaigu') 

elif (a<5): 
    print(a, 'zenbakia 5 baino txikiagoa da')
```

Azkenik `else` hitza ere existitzen da. Hau `if` edo `elif` batean ere sartu ez denean exekutatzen da soilik eta, horregatik, beti baldintza zikloaren amaieran idatzi behar da. 

```python title='else.py'
import random
a = random.randrange(10) # 0etik 9rako ausazko zenbakia

print('Tokatu zaigun zenbakia: ', a)
if (a==5): # hemen sartzen bada ez du hurrengo elif edo else konprobatuko
    print('5 tokatu zaigu') 

elif (a==4): # hemen sartzen bada ez du hurrengo else konprobatuko
    print('4 tokatu zaigu') 

else: # if-ean edo elif-ean sartu ez bada hemen sartuko da nahiz eta a='kaixo' izan
    print('ez zaigu ez 4 eta ez 5 tokatu')
```
