print("Hello!")
print("It is me you're looking for?")


# flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
# large_flowers = ['a large ' + f for f in flowers]
# #in english - for every thing in flowers, print 'a large' and the flower
# print(large_flowers)


# family = { 'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}
# my_family = {'my ' + potato + ' is ' + potato_chip for (potato,potato_chip) in family.items()}
# print(my_family)
# print(family.items())

class Zoo:
    """Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    """
    def __init__(self, name):
        self.zoo_name = name
        self.animals = dict()
        self.habitats = set()
        self.visitors = list()


    def build_habitat(self, name, type):
        """Adds tuples to the habitats set in the format (name, type)

        Method arguments:
        -----------------
        name(string) -- The marketing name of the habitat
        type(string) -- The type of habitat (e.g. Saltwater, Savanna, Swamp, etc.)
        """

        self.habitats.add((name, type))


    def sell_family_ticket(self, family):
        """Adds an entire family to the list of visitors

        Method argument:
        -----------------
        family(list) -- A list of people in a family of visitors
        """

        self.visitors.extend(family)


    def purchase_animal(self, type, name):
        """Add an animal to the zoo

        Method arguments:
        -----------------
        type(string) -- The type of animal to add
        name(string) -- The given name of the animal
        """

        self.animals[name] = type


    def list_animals(self):
        """Lists all animals in the zoo

        Method arguments:
        n/a
        """

        [print(k + ' the ' + v) for k, v in self.animals.items()]

    # def add_animal(animal, name):
      # pass



a_zoo = Zoo("Zoolandia")
a_zoo.purchase_animal("Tortoise", "Tommy")
a_zoo.list_animals()

a_zoo.list_animals.__doc__ # To view the docstring for the method
