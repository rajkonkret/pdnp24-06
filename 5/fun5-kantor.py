# stworzyc funkcje kantor
# ma posiadac dwie funkcje wewnętrzne usd, eur
# w zależnosci od parametru mamy otrzymywac właściwą funkcję
# mozliwosc przekazania dowolnej kwoty

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} dol na {kwota * 4.0} pln.")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur na {kwota * 4.31:.2f} pln.")

    if waluta == 'eur':
        return eur
    else:
        return usd


michal = kantor('usd')
klaudia = kantor('eur')

michal()
klaudia()
# Otwieram kantor
# Otwieram kantor
# Wymieniam dolary
# Wymieniam eur
michal(1000)  # Wymieniam 1000 dol na 4000.0 pln.
klaudia(100)