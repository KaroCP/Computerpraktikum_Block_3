# Computerpraktikum_Block_3
bei Herr Göddeke
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
# Aufgaben
Die AUFGABENSTELLUNG und ANWEISUNGEN Folder beinhaltet die Aufgabenstellung und weitere Hilfen zum Thema. Lies das Thema "Fraktale", das ist unser Thema. Die Einzelaufgaben sind:
- Newtonverfahren implementieren (Valentino)
- Beispiele suchen 
- Laufzeit verbessern, Insbesondere Zeiten vergleichen, Konvergenzordnung vergleichen (Momo)
- Interaktion implementieren (Karo)
- Ableitung und Nullstellenmenge symbolisch berechnen
- Andere Berechnungsverfahren implementieren (Valentino)
- Parameterabhängige Funktionen als Beispiele machen

# Aufteilung
Hier wird klargestellt wer was tut. Schreibt hier bitte immer rein, was ihr tut und am besten wie jeder euer Programmteile mit den anderen zu komunizieren hat. (Z.B. wenn's ein py-modul werden soll, das einfach erwähnen und wie es heißt...). Alle Dateinamen an denen ihr arbeitet, sollten in einer der folgenden Sektionen erwähnt werden.

## Allgemeiner Programmteil:
main: Ruft plot - die Plotfunktion von plot_stuff - auf. <br />

## Valentino
newton: Wird von plot_functions aufgerufen.

## Karo
plot_stuff: Ruft newton_approximation - das Newtonverfahren in newton - auf.

## Momo

