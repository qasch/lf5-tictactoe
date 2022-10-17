def do_something():
    foo = 3
    bar = 3
    sum = foo + bar
    # Ausgabe, keine Rückgabe!
    print("I did something: ", sum)


do_something()


# foo = 3
# bar = 2
# foo und bar sind Eingabeparameter
# diese werden beim Aufruf durch konkrete Werte (Argumente) ersetzt
# innerhalb der Funktion existieren die Paramenter als Variablen
def add(foo, bar):
    #      3  +   5
    sum = foo + bar
    return sum

to_print = add(3, 5928734)

print(to_print)

