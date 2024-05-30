import random
import matplotlib.pyplot as plt

class Lapin:
    def __init__(self, sexe):
        self.age = 0
        self.sexe = sexe
        self.semaines_sans_repas = 0
        self.nourriture_suffisante = True

    def manger(self):
        self.semaines_sans_repas = 0

    def vieillir(self):
        self.age += 1
        if not self.nourriture_suffisante:
            self.semaines_sans_repas += 1

    def est_vivant(self):
        max_age = 4 if not self.nourriture_suffisante else 6
        return self.age < max_age and self.semaines_sans_repas <= 2

    def peut_se_reproduire(self):
        return self.age >= 1 and self.nourriture_suffisante


class Carotte:
    def __init__(self, nombre):
        self.nombre = nombre

    def recolter(self, quantite):
        if self.nombre >= quantite:
            self.nombre -= quantite
            return quantite
        else:
            quantite_recoltee = self.nombre
            self.nombre = 0
            return quantite_recoltee


class Jardin:
    def __init__(self):
        self.lapins = [Lapin('M'), Lapin('F')]
        self.carottes = Carotte(200)
        self.semaine = 0

    def passer_semaine(self):
        self.semaine += 1

        # Nourrir les lapins
        for lapin in self.lapins:
            if self.carottes.nombre > 0:
                lapin.manger()
                self.carottes.recolter(1)
            else:
                lapin.nourriture_suffisante = False

        # Vieillir et vérifier les lapins
        self.lapins = [lapin for lapin in self.lapins if lapin.est_vivant()]

        # Reproduction des lapins
        males = [lapin for lapin in self.lapins if lapin.sexe == 'M' and lapin.peut_se_reproduire()]
        femelles = [lapin for lapin in self.lapins if lapin.sexe == 'F' and lapin.peut_se_reproduire()]
        if males and femelles:
            for femelle in femelles:
                if self.semaine % 52 == 16 or self.semaine % 52 == 27:
                    for _ in range(6):
                        self.lapins.append(Lapin(random.choice(['M', 'F'])))

    def simuler(self, annees):
        population_lapins = []
        population_carottes = []

        for _ in range(annees * 52):
            self.passer_semaine()
            population_lapins.append(len(self.lapins))
            population_carottes.append(self.carottes.nombre)

            # Ajouter des carottes en mars (semaine 9)
            if self.semaine % 52 == 9:
                self.carottes.nombre += 200

        return population_lapins, population_carottes


# Simulation
jardin = Jardin()
population_lapins, population_carottes = jardin.simuler(6)

# Tracer les résultats
plt.figure(figsize=(14, 7))
plt.plot(population_lapins, label='Population de lapins')
plt.plot(population_carottes, label='Population de carottes')
plt.xlabel('Semaines')
plt.ylabel('Population')
plt.legend()
plt.title('Évolution des populations de lapins et de carottes sur 6 ans')
plt.show()
