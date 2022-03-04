class Film(object):
    def __init__(self, titlu, durata):
        self.titlu = titlu
        if durata <= 180:
            self.durata = durata
        else:
            raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute. ")

    def afisare_filme(self):
        # return(f"Filmul {self.titlu} ruleaza in cinematograf cu o durata de {self.durata} minute. " )
        raise NotImplementedError("Nu ati introdus ce filme vor rula in cinematograf. ")
