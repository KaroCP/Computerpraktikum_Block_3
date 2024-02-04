# Computerpraktikum_Block_3
bei Herr Göddeke
# Ausführen
(Für Karos Part): Führe die main Datei aus und folge den Anweisungen in der Konsole. <br>
Hinweis: Für Anzahl an Punkten "density" höchstens 200 angeben, sonst dauert das echt lange. <br>
Manuelle Schalter im Programm (noch verläufig, noch nicht sicher, wie es langfristig gelöst werden soll.):
- "fix_data" in main: Wenn True wird aus einer gegebenden Menge an Beispiel_funktionen die Funktion gewählt; Wenn False wird auf das bisherige x^n-1 Polynom zurückgegriffen.
  (Beides fragt in der Konsole noch eine Zahl ab, welche Funktion aus der Beispielklasse verwendet werden soll.)
# Aufgaben
Die AUFGABENSTELLUNG und ANWEISUNGEN Folder beinhaltet die Aufgabenstellung und weitere Hilfen zum Thema. Lies das Thema "Fraktale", das ist unser Thema. Die Einzelaufgaben sind:
- Newtonverfahren implementieren (Valentino)
- Beispiele suchen (Karo)
- Laufzeit verbessern, Insbesondere Zeiten vergleichen, Konvergenzordnung vergleichen (Momo)
- Interaktion implementieren (Karo)
- Ableitung symbolisch berechnen (Momo?)
- Andere Berechnungsverfahren implementieren (Valentino)
## (aktuelle) TODOs:
- Bericht für das Projekt schreiben. https://www.overleaf.com/project/65bfa1bcc677b426a3b87741
- Was machen wir mit dem manuellen Toggler "fix_data"?
- Zeitmessung: Wie hängt die Berechnungszeit von der density ab. <br>
  An sich erstmal für den Bericht. Ich fände es aber auch cool, wenn man eine Abschätzung für Berechnungsdauer printen lassen könnte (abhängig von der letzten Berechnungsdauer und der gewünschten Neuberechnung).
- Symbolische Berechnung der Ableitung einfügen. Und (über sympy) Einlesen einer beliebigen Funktion in der Konsole.
- Automatischen Zoom (=Animation?) machen
## Weitere Ideen
- Parameterabhängige Funktionen als Beispiele machen
- Adaptive Max_Iteration (großes Max Iterarion und durch np.max teilen)
- Beispiele (Kreisteilungspolynome gebrochen rationale Funktionen, trigonometrisch)
- Dynamisches Berechnen (für rauszoomen) d.h. nutzt die schon berechneten Pixel 
# Aufteilung
Hier wird klargestellt wer was tut. Schreibt hier bitte immer rein, was ihr tut und am besten wie jeder euer Programmteile mit den anderen zu komunizieren hat. (Z.B. wenn's ein py-modul werden soll, das einfach erwähnen und wie es heißt...). Alle Dateinamen an denen ihr arbeitet, sollten in einer der folgenden Sektionen erwähnt werden.

## Valentino
### newton
Die Funktion newton_approx wird von color_newton in functions aufgerufen.

## Karo
Hier kurze Beschreibung der Module. Für genauere Informationen siehe Python Documentation.
### main
Erstellt mithilfe von data_collection importierten Funktionen ein Fractal und gibt den Nutzer Informationen, wie mit dem Plot interagiert werden kann.
### functions
Definiert die Klasse Fractal, die Daten wie die genutze Funktion oder das Iterationslevel speichert, den Plot erstellt und die Möglichkeit der Interaktion mit dem Plot definiert.<br>
Die Funktion (genauso wie ihre Ableitung) werden als Lambdafunkktionen in einer komplexen Zahl eingegeben (z.B. f = lambda z:z**3-1).<br>
Die Klasse ruft zur Berechnung des Plots - je nach Einstellung - die Funktion newton_approx in newton_von Valentino oder newton_with_matrices in newton_works auf.
### data_collection
Sammelt und erstellt mögliche Daten für Fraktale. Und definiert Funktionen debug-Funktionen, durch die der Nutzer - mithilfe der Konsole - einen Datensatz auswählen kann.
### newton_works
Eine mögliche Implementation für den Newton Algorithmus.

## Momo
### Programmteil/e : newton (revisited). (saad :-( )
### [Datei/Ordner]
ORDNER : "newton_c++"
### [BESCHRIEBUNG-newton (rewisited)]	
Ich werde das selbe wie Valentino machen, nu rin C++. Es wird sich um ein Programm [.exe] handeln, die in python aufgerufen werden kann, zb:
```
import subprocess
subprocess.run(["/newton_c++.exe", "KARO's INPUT"])
```
Dann wird in der Varibale "return_value"
### [DOKUMENTATION-newton (rewisited)]
Der INPUT kommt von KARO's "main.py" (also zb):
```
import subprocess
subprocess.run(["/newton_c++.exe", "KARO's INPUT"])
```
der INPUT ist von der Form:
 <br>[
 <br>
__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; __ <br>
| [x_1,y_1] & [x_1, y_2] & ...   | <br>
| [x_2,y_1] & [x_2, y_2] & ...   | <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
|__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      __| <br>
 <br>
, <br>
[FUNKTION]
 <br>
 <br>] <br>
also eine mxn Matrix ist  <br>

Wobei der INDEX von zB "[x_1,y_1]" (also 1,1), der INDEX des PIXELS aus dem resultierenden Bild ist, und "x_1,y_1" entsprechend der Realteil und Imaginärteil der Zahl "z" aus der Gausebene ist, die ausgewertet werden soll.
<br>
der OUTPUT ist eine Matrix <br>
 <br>
__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; __ <br>
| [r_11,g_11,b_11] & [r_12,g_12,b_12] & ...   | <br>
| [r_21,g_21,b_21] & [r_22,g_22,b_22] & ...   | <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
| . &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	| <br>
|__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      __| <br>
<br>
Im Grunde also das Bild, als matrix codiert.

### [BESCHREIBUNG-functions]
Definiert die Klasse Funktionen und wird von allen anderen Dateien aufgerufen. MOMO's AUFGABE: zwei kleine Änderungen an der "functions.py" (KARO macht eig das meiste) ich mache nur das ABLEITEN mit sympy oder so

### [DOKUMENTAATION-functions]
TO BE DONE
<br>
# So arbeitet ihr mit github:
## Erstes Mal: 
 1) Installiere das Programm "git" z.B von der Seite :https://gitforwindows.org/
 2) Eröffne eine lokale Repository mit dem Befehl : "git init".
 3) Gebe den anderen Bescheid, dass du das bist mit dem Befehl : "git config --global user.name "[your_name]". ([your_name] soll ersetzt werden mit dem Namen den die anderen sehen sollen.)
## Runterladen:
 1) Navigiere in den Ordner auf deinem PC, in dem deine lokale Kopie des Projektes gespeichert werden soll. Tippe dafür in das Progremm CMD, den Befehl : "cd [PATH]" also zum beispiel auf dem Desktop :"cd C:\Users\USER_NAME\Desktop\test" (USER_NAME ist euer Windows Benutzername)
    (Wer Schwiereigkeiten hat die Addresse von seinem gewünschten Ordner zu finden kann einfach im Explorer den Link kopieren, oder fragen :))
 3) Lade die bisherigen Dinge aus der online Repository herunter mit dem Befehl : "git pull https://github.com/KaroCP/Computerpraktikum_Block_3". (Jedes Mal, bevor du an deinem Code arbeitest, solltest du diesen Befehl ausführen, um auf dem neusten Stand zu sein.)
## Hochladen:
 1) Wenn du fertig mit coden bist, benutze den Befehl "git add .".
 2) Im Anschluss benutze den Befehl "git commit -m 'MESSAGE'". (MESSAGE ist eine optionale Nachricht die z.B mit deiner Veränderung am Code zu tun hat.)
 3) Lade dein Ergebniss hoch mit dem Befehl : "git push https://github.com/KaroCP/Computerpraktikum_Block_3".
