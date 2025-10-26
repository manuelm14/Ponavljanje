def kreiraj_pozdrav(ime):
    pozdravna_poruka=f"Pozdrav, {ime}!"
    return pozdravna_poruka
pozdrav_za_anu=kreiraj_pozdrav("Ana")
pozdrav_za_luku=kreiraj_pozdrav("Luka")
print(pozdrav_za_anu)
print(pozdrav_za_luku)