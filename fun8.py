def all_aparams(a, b, /, c=76, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


all_aparams(1, 2)  # argumenty po pozycji
# po dodaniu /
# a i b mogą byc tylko po pozycji bo są z lewej strony /
# all_aparams(b=8, a=9)  # argumenty po nazwie, TypeError: all_aparams() got some positional-only arguments passed as keyword arguments: 'a, b'
all_aparams(1, 2, 3, 5)  # c, d 3 5
all_aparams(1, 2, c=3, d=5)  # c, d 3 5


def allparams_2(a, b, /, c=42, *args, d=567, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


# ile minimum arg? dwa a i b, obowiązkowo po pozycji
allparams_2(1, 2)
# a, b 1 2
# c, d 42 567
# args ()
# kwargs {}

# jak przekazac dane do c?
allparams_2(1, 2, c=90)
allparams_2(1, 2, 90)
# a, b 1 2
# c, d 90 567
# args ()
# kwargs {}

# jak przekazac cokolwiek do *args?
allparams_2(1, 2, 3, 4)
# a, b 1 2
# c, d 3 567
# args (4,)
# kwargs {}
# czy wtedy c mozemy przekazac po nazwie? NIE - pozycyjne nie mogą byc po nazwanych
# allparams_2(1,2,c=9,4)

# kiedy zakończy sie wpisywanie danych do *args? dopiero po jawnym wskazaniu, ze chcemy cos wpisac do d
# dane do zmiennej d muszą byc po nazwie bo są po *args
allparams_2(1, 2, 3, 4, 5, 6, 7, 8, 9, 210, 11, 1, 1, 1, 1, d=89)
# a, b 1 2
# c, d 3 89
# args (4, 5, 6, 7, 8, 9, 210, 11, 1, 1, 1, 1)
# kwargs {}

# jak przekazac do **kwargs?
allparams_2(1, 2, 3, 4, 5, 6, 7, 8, 9, 210, 11, 1, 1, 1, 1, d=89, name="Radek", g=90, h=123)
# a, b 1 2
# c, d 3 89
# args (4, 5, 6, 7, 8, 9, 210, 11, 1, 1, 1, 1)
# kwargs {'name': 'Radek', 'g': 90, 'h': 123}
allparams_2(1, 2, name="Radek", g=90, h=123)
# a, b 1 2
# c, d 42 567
# args ()
# kwargs {'name': 'Radek', 'g': 90, 'h': 123}

# gdzie trafi a?
allparams_2(1, 2, name="Radek", g=90, h=123, a=88)
# a, b 1 2
# c, d 42 567
# args ()
# kwargs {'name': 'Radek', 'g': 90, 'h': 123, 'a': 88}