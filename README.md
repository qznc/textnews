# Text News

Nachrichten als reine Text in puristischer Website.
[Online auf NeoCities](https://textnews.neocities.org/).

## Warum?

Weil gerade auf Smartphones mit langsamer Verbindung
das Nachrichtenlesen frustrierend ist.
TextNews ist nur Text, der mit einem einzigen Request geladen wird.
Üblicherweise dauert DNS-Auflösung und Verbindungsaufbau länger
als das Herunterladen der Daten.

* https://danluu.com/web-bloat/
* http://www.drudgereport.com/

## Benutzung

Zur Erstellung einer HTML Datei:

  ./generate.py index.html

Es werden immer höchstens die letzten 24 Stunden an Nachrichten angezeigt.
Nachmittags wird der Vortag gar nicht mehr angezeigt.
Nachrichten der letzten zwei Stunden werden hell-gelb hinterlegt.

Sortiert wird, indem manche Wörter positiv bzw negativ gewertet werden.
Das ist ein sehr naives Verfahren, aber funktioniert ok.

Die Version [online auf NeoCities](https://textnews.neocities.org/)
wird stündlich neu generiert.
Man sieht im Titel, wann genau das war.
Häufiger als stündlich nachzusehen ist also sinnlos.
