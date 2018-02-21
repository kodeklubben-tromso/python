X - Passordbeskyttelse
---

For å gjøre dette så må vi lære om matematiske funksjoner som kalles `Hash funksjoner`.


### Hash
---
En `Hash` er en slags kode. For å lage en `Hash` så bruker vi matematiske funksjoner som oversetter fra en rekke med tall, til en slags nøkkel som har en bestemt lengde.
Som vi sikkert husker fra tidligere så er tekst i en datamaskin, egentlig bare en rekke tall. Det vil si at vi kan oversette tekst også:

```python
import hashlib

tekst = "Hei, dette er en uhashet tekst"
hash = hashlib.sha256(tekst).hexdigest()
print hash

3d1af6aabea17a86a1afdde989d3b27f599542820cd307c3733c8f6d46ec6250
```
Som vi ser så har teksten min `"Hei, dette er en uhashet tekst"` blitt oversatt til `3d1af6aabea17a86a1afdde989d3b27f599542820cd307c3733c8f6d46ec6250`. 

Det som er nyttig med en slik funksjon, er at det er nesten umulig å regne seg tilbake til den opprinnelige teksten fra den nye `Hashen`. Det betyr at når vi har oversatt teksten vår, så må man vite teksten på forhånd for å lage den samme hashen igjen. En annen viktig egenskap, er at hver gang vi hasher teksten `"Hei, dette er en uhashet tekst"` med `SHA256`, så vil vi alltid få det samme resultatet. Men hvis vi forandrer en bokstav i teksten, så vil resultatet se helt forskjellig ut:

```python
# Her har vi lagt til et punktum helt til slutt
ny_tekst = "Hei, dette er en uhashet tekst."

hash = hashlib.sha256(ny_tekst).hexdigest()
print hash

65e555e99035a2deca38f6c9d6a825700b0ff7c4959927e389e7920396f869af
```


### Passord
---
Når man skal logge inn på en nettside, så bør man ikke sende passordet sitt over nett. Hvis noen får tak i den samtalen som du har med nettsiden, så vil den som overvåker deg, få tak i passordet ditt.

Vanligvis så vil man lage en `Hash` av passordet sitt, og så sende den over nettet istedet. Hvis noen får tak i `Hashen` av passordet ditt, så vil de uansett ikke klare å finne ut passordet. Nettsiden man snakker med, trenger ikke å vite passordet ditt, så lenge den vet `Hashen` av passordet ditt.