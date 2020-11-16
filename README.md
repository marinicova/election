# election

Daný projekt stáhne do csv souboru volební výsledky pro každou obec zvoleného okresu.

Na nasledujíci stránke [volby](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)
se okresy vybírají přes X ve sloupci Výběr obce.

Skript očekává dva vstupy:
- adresu 
- nazev souboru, který vytvoří a uloží doň data
    
**Adresa potřebná pro správne fungovaní skriptu** je například:
- pro okres Praha: <https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100>

Nakonec skript vytvoří csv soubor. 
