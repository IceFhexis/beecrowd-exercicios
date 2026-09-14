# ler as três características
tipo = input()
classe = input()
alimentacao = input()

animais = {
    ("vertebrado", "ave", "carnivoro"): "aguia",
    ("vertebrado", "ave", "onivoro"): "pomba",
    ("vertebrado", "mamifero", "onivoro"): "homem",
    ("vertebrado", "mamifero", "herbivoro"): "vaca",
    ("invertebrado", "inseto", "hematofago"): "pulga",
    ("invertebrado", "inseto", "herbivoro"): "lagarta",
    ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
    ("invertebrado", "anelideo", "onivoro"): "minhoca"
}

animal = animais[(tipo, classe, alimentacao)]

print(animal)