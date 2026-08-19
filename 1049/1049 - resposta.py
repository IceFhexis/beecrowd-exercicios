# ler as caracteristicas e filtrar qual ser vivo é 
# ler as três características
tipo = input()
classe = input()
alimentacao = input()

# primeiro: vertebrado ou invertebrado?
if tipo == "vertebrado":

    # se for vertebrado, pode ser ave ou mamífero
    if classe == "ave":

        if alimentacao == "carnivoro":
            print("aguia")
        else:
            print("pomba")

    else:  # mamifero

        if alimentacao == "onivoro":
            print("homem")
        else:
            print("vaca")

else:  # invertebrado

    # se for invertebrado, pode ser inseto ou anelídeo
    if classe == "inseto":

        if alimentacao == "hematofago":
            print("pulga")
        else:
            print("lagarta")

    else:  # anelideo

        if alimentacao == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")