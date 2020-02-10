class Country:

    def __init__(self, name,population, area):
        self.name = name
        self.population = population
        self.area = area


    def is_large(self,other):
        return self.area > other.area


    def population_density(self):
        return self.population / self.area

    def __str__(self):
        return '{} has a population of {} and is {} square km.'. format(self.name, self.population, self.area)


    def __repr__(self):
        return "Country ('{}','{}','{}'".format(self.name, self.population, self.area)



spain = Country('Spain', 46660000,505990)
germany =Country('Germany',82790000,357386)

print("Is Spain more large than Germany?")
print(spain.is_large(germany))

print("Is Germany more large than Spain?")
print(germany.is_large(spain))

print(spain.population_density())

print(spain.__repr__())
print(germany.__repr__())
print(spain.__str__())
print(germany.__str__())





