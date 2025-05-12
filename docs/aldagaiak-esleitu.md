# ALDAGAIAK ESLEITU

Gure kodean zehar aldagai ezberdinak beharko ditugu beti. Horregatik, hauek nola esleitzen diren jakin behar dugu. 

!!! tip "TEORIA: Nola esleitu aldagai bat"
    Aldagaia kutxa baten moduan irudikatu dezakegu gure buruan, barruan balio bat duena. Formatua:
    ```text
    guk_jarritako_aldagaiaren_izena = aldagaiaren_balioa
    ```
## ADIBIDEAK
<hr>

### :arrow_right: 1.ADIBIDEA: ALDAGAIA ESLEITU

Kasu honetan `batura` izeneko aldagiaean `5` edukiko dugu gordeta.
```python title="aldagaien_esleipena.py"
lehen_aldagaia = 2
bigarren_aldagaia = 3
batura = lehen_aldagaia + bigarren_aldagaia
print(batura)
```

### :arrow_right: 2.ADIBIDEA: ALDAGAIA BERRESLEITU

Kasu honetan `batura` izeneko aldagiaean `7` edukiko dugu gordeta.
`lehen_aldagaia` kutxatxoan gauza bakarra eduki dezakegu gordeta, eta kodea goitik
behera irakurtzen denez, esleitu diogun azkena gordeko du. 
```python title="aldagaien_berresleipena.py"
lehen_aldagaia = 2
bigarren_aldagaia = 3
lehen_aldagaia = 4
batura = lehen_aldagaia + bigarren_aldagaia
print(batura)
```

## JARRI PRAKTIKAN
<hr>

Kopiatu kode hau zure ordenagailuan:

```text
import random
a = random.randrange(10)
b = random.randrange(10)

# Zure kodea hemen joango da

```
Kode honek a eta b aldagaiei 1etik 10erako ausazko zenbaki bat esleitzen die.


Kodea exekutatzean inprimatuta espero den emaitzaren antzekoa jarraian agertzen da. *Ez dakit pythonek ze zenbaki emango dituen ausaz, beraz ez dakit emaitza zehatza, baina formatua errespetatu. Kodea exekutatzen duzun bakoitzean emaitza ezberdin bat edukiko duzu, baina beti zentzuzkoa izan behar da*. 

```sh
============
BATUKETA
============
10+4=14

============
KENKETA
============
10-4=6

```