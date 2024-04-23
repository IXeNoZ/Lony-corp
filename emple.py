import random
import matplotlib.pyplot as plt

class Lapin:
    def __init__(self):
        self.age = 0
        self.faim = 0

    def vieillir(self):
        self.age += 1
        self.faim += 1

    def manger(self):
        self.faim = 0

    def est_vivant(self):
        return self.faim <= 2 and (self.age <= 4 if self.faim > 0 else self.age <= 6)

    def peut_se_reproduire(self):
        return self.age >= 1

class Jardin:
    def __init__(self):
        self.lapins = []
        self.carottes = 200
        self.population_lapins = []
        self.population_carottes = []

    def ajouter_lapin(self, lapin):
        self.lapins.append(lapin)

    def simuler_semaine(self):
        for lapin in self.lapins:
            lapin.vieillir()
            if self.carottes > 0:
                lapin.manger()
                self.carottes -= 1
        self.lapins = [lapin for lapin in self.lapins if lapin.est_vivant()]
        if len(self.lapins) >= 2 and all(lapin.peut_se_reproduire() for lapin in self.lapins):
            self.lapins.extend(Lapin() for _ in range(6))
        self.population_lapins.append(len(self.lapins))
        self.population_carottes.append(self.carottes)

    def simuler_jardin(self, annees=6):
        for _ in range(52 * annees):
            self.simuler_semaine()
            if _ % 52 == 12:
                self.carottes += 200

    def tracer_evolution(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.population_lapins, label='Population de lapins', color='b')
        plt.plot(self.population_carottes, label='Quantité de carottes', color='g')
        plt.xlabel('Semaines')
        plt.ylabel('Population / Quantité')
        plt.title('Évolution de la population de lapins et de carottes')
        plt.legend()
        plt.show()

# Simulation
jardin = Jardin()
lapin_m = Lapin()
lapin_f = Lapin()

jardin.ajouter_lapin(lapin_m)
jardin.ajouter_lapin(lapin_f)

jardin.simuler_jardin()
jardin.tracer_evolution()