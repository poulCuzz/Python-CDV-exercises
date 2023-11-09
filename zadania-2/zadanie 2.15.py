slownik = {"m1": "Ford", "m2": "Fiat", "m3": "Opel", "m4": "Skoda", "m5": "Wołga", "m6": "Dacia"}
copyslownik = slownik.copy()
slownik.items()
update = {"m7": "FSO"}
slownik.update(update)
slownik.clear()
print(slownik)