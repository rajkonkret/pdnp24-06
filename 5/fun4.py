# funkcja wewnętrzna, zagnieżdzona
#

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres pamięci (referencje)


fun1()  # To jest fun1
print(fun1())  # <function fun1.<locals>.fun2 at 0x0000021A213A9E40>
print(type(fun1()))  # <class 'function'>
xFun = fun1()  # w tej zmiennej będzie fun2 at 0x0000021A213A9E40 czyli adres fun2
xFun()


