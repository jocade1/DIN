class Continent:
    def __init__(self, name,Countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        total = 0
        for country in self.countries:
            total += country.population

        return total