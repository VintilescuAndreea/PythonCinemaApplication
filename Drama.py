from Film import Film

class Drama(Film):
    def __init__(self, titlu, durata, varsta_minima):
        super().__init__(titlu, durata)
        self.varsta_minima = varsta_minima

    def afisare_filme(self):
        return(f"Drama cu titlul {self.titlu} si durata de {self.durata} minute ruleaza in cinematograf pentru persoanele" \
               f" cu varsta minima de {self.varsta_minima} ani. ")

