# działania na plikach
# context manager - usprawnia pracę np.:  z plikami
# with - context manager w pythonie
# open() - operacje na plikach

# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # fh - filehandler, opiekun pliku
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")
# w tworzy nowy plik, nadpisuje istniejacy
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Nadpisane\n")

# a - dopisanie na końcu pliku
with open('test.log', 'a', encoding='utf-8') as f:
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dośdane\n")
    f.write("Żółć\n")

with open('test.log', 'r', encoding="utf-8") as file:
    lines = file.read()

print(lines)
# DoĹ›dane
# po dodaniu  encoding="utf-8"
# Dośdane
