# NOLA IRAKURRI KODEA?

## Ordena
<hr>
Pythonen beti goitik behera eta ezkerretik eskuinera exekutatuko da kodea. Hau da, ez da 3.lerroa exekutatuko 2.neko guztia amaitu arte.

Kode honek errorea emango dit. Mezua inprimatzen saiatzen ari gara, baina oraindik ez du ikasi zein den mezua:

```python title="ordena.py"
print(mezua)
mezua="Kaixo mundua"
```

## Indentazioa
<hr>
Alineazioak garrantzia handia du Pythonen.

Ondoko adibidean `bigarren_aldagaia` tab 1 barrurago dagoenez, errorea emango digu:
```python title="alineazioa.py"
lehen_aldagaia = 2
    bigarren_aldagaia = 3
batura = lehen_aldagaia + bigarren_aldagaia
```

!!! note "OHARRA"
    4 espazio = tab 1
## Kodea komentatu
<hr>
Kodea handitzen doan heinean, zati bakoitzak zer egiten duen azaltzea garrantzitsua da. Hau ez da kodearen parte izan behar, hau da, pythonek ez ditu exekutatu behar. Bi modu daude: bloke komentarioak `'''` artean edo lerro bakarreko komentarioak `#` sinboloaren ondoren.

```python title="komentarioak.py"
'''
Hau bloke komentario bat da. 
Nahi ditudan lerroak idatzi ditzaket
===========================
BI ALDAGAIEN BATURA:
===========================
'''
lehen_aldagaia = 2
bigarren_aldagaia = 3
# Hau lerro bakarreko komentarioa da.
# Beste lerro bat komentatu nahi badut beste # bat idatzi behar da
# Baturaren kalkulua:
batura = lehen_aldagaia + bigarren_aldagaia
```

!!! note "OHARRA"
    Kode honek ez du ezer inprimatuko, ez baitugu `print()` erabili.




 
