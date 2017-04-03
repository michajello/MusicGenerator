# Programowanie w jezyku Python 2016/2017 zadanie 1

Uporczywe narkotyczne melodie potrafią czasem na długo przylgnąć do umysłu.
Napisz program, który generuje narkotyczne melodie. Program powinien generować różne melodie w zależności od tego, jakie użytkownik poda opcje. Użytkownik będzie tak długo modyfikował opcje programu aż wygenerowana melodia utkwi mu na stałe w głowie.

Melodie te powinny być generowane w postaci plików midi i zapisywane na dysku twardym, przy czym użytkownik powinien mieć możliwość podania lokalizacji. Obsługa karty dźwiękowej w celu odtworzenia wygenerowanej melodii nie jest konieczna. Można użyć dowolnej biblioteki do obslugi formatu midi, przykladowo https://pypi.python.org/pypi/miditime


Program ten powinien wykorzystywać następujące elementy:
 - klasy
 - funkcje
 - parsowanie argumentów linii poleceń za pomocą modułu argparse ze standardowej biblioteki
 - zewnętrzna biblioteka do obsługi formatu midi

Tresc zadania w Google Drive: https://goo.gl/dbfwo3

Termin oddania zadania: 3 kwietnia 2017, 20:00

#Requirements:
Python 3.6
python3-tk

Libraries:
miditime 1.1.3
pillow 3.1.2
matplotlib 2.0.0

**Music Generator** can generate random music or 'translate' pictures into music:
    usage: main.py [-h] [-f FILENAME] [-l LENGTH] [-s SPEED] [-r {1,2,3,4,5,6}]
        or
    main.py [-h] [-f FILENAME] [-l LENGTH] [-s SPEED]  [-i IMAGE]
    
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Name of output file
  -l LENGTH, --length LENGTH
                        Length of song in seconds
  -s SPEED, --speed SPEED
                        Beats per minute
  -r {1,2,3,4,5,6}, --rate {1,2,3,4,5,6}
                        Narkotic rate; allowed values:[1,2,3,4,5,6]
  -i IMAGE, --image IMAGE
                        Image to convert into music


