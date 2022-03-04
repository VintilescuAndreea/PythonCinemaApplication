from Film import Film

class Animatie(Film):
    def __init__(self, titlu, durata, limba_dublare):
        super().__init__(titlu, durata)
        self.limba_dublare = limba_dublare

    def afisare_filme(self):
        return (f"Animatia cu titlul {self.titlu} si durata de {self.durata} minute ruleaza in cinematograf dublat in limba " \
                f"{self.limba_dublare}. ")

