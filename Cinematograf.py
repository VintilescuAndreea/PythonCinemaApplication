import random
from Film import Film
from Animatie import Animatie
from Drama import Drama

class Cinematograf(object):
    def __init__(self, lista_filme):
        self.lista_filme = lista_filme

    def adaugare_film(self, film):
        self.lista_filme.append(film)

    def afisare_filme(self):
        print("Acestea sunt filmele care ruleaza in Cinematograf: " + "\n")
        for film in self.lista_filme:
            print(film.afisare_filme())

    def afisare_animatii(self):
        print("Acestea sunt animatiile care ruleaza in Cinematograf: " + "\n")
        for film in self.lista_filme:
            if isinstance(film, Animatie):
                print(film.afisare_filme())

    def alegere_film_aleator(self):
        return random.sample(self.lista_filme, 1)

    def salvare_filme(self, filme_salvate):
        with open(file= filme_salvate, mode = "w") as file:
            for film in self.lista_filme:
                if isinstance(film, Animatie):
                    file.write("Titlul: " + film.titlu + ", durata: " + str(film.durata) + ", dublat in limba: " + film. limba_dublare + "\n")
                elif isinstance(film, Drama):
                    file.write("Titlul: " + film.titlu + ", durata: " + str(film.durata) + ", varsta minima: " + str(film.varsta_minima) + "\n")

listafilme = []
cinema = Cinematograf(listafilme)

while True:
    comanda = input("Ce comanda doriti sa efectuati? ")
    if comanda == "adauga_drama":
        titlu_drama = input("Ce titlu are drama? ")
        durata_drama = int(input(" Ce durata are drama? "))
        varsta_min_drama = int(input("Care este varsta minima pentru aceasta drama? "))
        drama = Drama(titlu_drama,durata_drama, varsta_min_drama)
        cinema.adaugare_film(drama)
    elif comanda == "adauga_animatie":
        titlu_animatie = input("Ce titlu are animatia? ")
        durata_animatie = int(input(" Ce durata are animatia? "))
        limba_dublare_animatie = input("In ce limba este dublata animatia? ")
        animatie = Animatie(titlu_animatie, durata_animatie, limba_dublare_animatie)
        cinema.adaugare_film(animatie)
    elif comanda == "afisare":
        cinema.afisare_filme()
    elif comanda == "afisare_animatii":
        cinema.afisare_animatii()
    elif comanda == "alege_film":
        film_aleator = cinema.alegere_film_aleator()
        print(cinema.alegere_film_aleator())
        print("Titlul filmului ales aleator: " + film_aleator[0].titlu )
    elif comanda == "salveaza_filme":
        fisier_filme_salvate = input("Care este numele fisierului in care doriti sa salvati filmele? ")
        cinema.salvare_filme(fisier_filme_salvate)
    elif comanda == "rezolvare cerinte":
        listacufilme =[]
        cinema_cerinte = Cinematograf(listacufilme)

        drama1 = Drama("American Beauty", 122, 12)
        drama2 = Drama("The Curious Case of Benjamin Button", 166, 15 )
        drama3 = Drama("Hachiko: A Dog's Story", 93, 12 )
        cinema_cerinte.adaugare_film(drama1)
        cinema_cerinte.adaugare_film(drama2)
        cinema_cerinte.adaugare_film(drama3)


        animatie1 = Animatie("Madagascar", 86, "romana")
        animatie2 = Animatie("Ratatouille", 110, "engleza")
        animatie3 = Animatie("Shrek", 92, "romana")
        cinema_cerinte.adaugare_film(animatie1)
        cinema_cerinte.adaugare_film(animatie2)
        cinema_cerinte.adaugare_film(animatie3)

        cinema_cerinte.salvare_filme("fisier_filme_cerinta.txt")
        with open('fisier_filme_cerinta.txt', 'r+') as file:
            print(file.read())

        film_aleator = cinema_cerinte.alegere_film_aleator()
        if isinstance(film_aleator[0] , Animatie):
            print("Titlul filmului aleator: " + film_aleator[0].titlu + ", durata: " + str(film_aleator[0].durata) + \
                  ", limba in care s-a dublat: " + film_aleator[0].limba_dublare)
        if isinstance(film_aleator[0], Drama):
            print("Titlul filmului aleator: " + film_aleator[0].titlu + ", durata: " + str(film_aleator[0].durata) + \
                  ", varsta minima: " + str(film_aleator[0].varsta_minima) + "\n")
    elif comanda == "exit":
        break
    else:
        print("Comanda introdusa nu este valida. ")
        continue


