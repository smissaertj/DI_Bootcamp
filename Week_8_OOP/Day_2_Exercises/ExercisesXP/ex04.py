"""
Exercise 4 : Afternoon At The Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
"""

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.sorted_animals = sorted(self.animals)
        self.grouped_animals = {}

        self.key = 1
        for animal in self.sorted_animals:
            print(animal)
            self.grouped_animals[len(self.grouped_animals) + 1] = [animal]


        print(self.grouped_animals)


my_zoo = Zoo('myzoo')
my_zoo.add_animal('Ape')
my_zoo.add_animal('Aardvark')
my_zoo.add_animal('Bear')
my_zoo.add_animal('Baboon')
my_zoo.sort_animals()