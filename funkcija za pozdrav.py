def kreiraj_pozdrav(ime):
    pozdravna_poruka=f"Pozdrav, {ime}!"
    return pozdravna_poruka
pozdrav_za_mariju=kreiraj_pozdrav("Marija")
pozdrav_za_luku=kreiraj_pozdrav("Luka")
print(pozdrav_za_mariju)
print(pozdrav_za_luku)
