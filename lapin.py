import random
import matplotlib.pyplot as plt

class Lapin:
    def __init__(self, age=0, sex='M', hungry_weeks=0):
        self.age = age
        self.sex = sex
        self.hungry_weeks = hungry_weeks
        self.alive = True

    def age_one_week(self):
        if self.alive:
            self.age += 1
            self.hungry_weeks += 1
            if self.hungry_weeks > 2:
                self.alive = False
            elif self.age > 6 * 52:
                self.alive = False
            elif self.age > 4 * 52 and self.hungry_weeks > 0:
                self.alive = False

    def feed(self):
        self.hungry_weeks = 0

    def can_reproduce(self):
        return self.alive and self.age >= 52

class Carotte:
    def __init__(self):
        self.harvested = False

class Jardin:
    def __init__(self):
        self.lapins = [Lapin(sex='M'), Lapin(sex='F')]
        self.carottes = [Carotte() for _ in range(200)]
        self.week = 0

    def simulate_week(self):
        # Aging and feeding rabbits
        for lapin in self.lapins:
            lapin.age_one_week()
            if lapin.alive:
                if self.carottes:
                    lapin.feed()
                    self.carottes.pop(0)

        # Reproduction in April and July
        if self.week % 52 == 16 or self.week % 52 == 29:
            males = sum(1 for lapin in self.lapins if lapin.alive and lapin.sex == 'M' and lapin.can_reproduce())
            females = sum(1 for lapin in self.lapins if lapin.alive and lapin.sex == 'F' and lapin.can_reproduce())
            pairs = min(males, females)
            for _ in range(pairs * 6):
                sex = 'M' if random.random() < 0.5 else 'F'
                self.lapins.append(Lapin(sex=sex))

        # Harvesting carrots in June
        if self.week % 52 == 14:
            self.carottes.extend(Carotte() for _ in range(200))

        self.week += 1

    def simulate_years(self, years):
        rabbit_population = []
        carrot_population = []

        for _ in range(years * 52):
            self.simulate_week()
            rabbit_population.append(len([lapin for lapin in self.lapins if lapin.alive]))
            carrot_population.append(len(self.carottes))

        return rabbit_population, carrot_population

# Simulate 6 years
jardin = Jardin()
rabbit_population, carrot_population = jardin.simulate_years(6)

# Plot the populations
plt.figure(figsize=(12, 6))
plt.plot(rabbit_population, label='Lapins')
plt.plot(carrot_population, label='Carottes')
plt.xlabel('Semaines')
plt.ylabel('Population')
plt.legend()
plt.title('Évolution des populations de lapins et de carottes sur 6 ans')
plt.show()