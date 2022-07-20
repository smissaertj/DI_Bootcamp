class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, name, mount=1):
        if name in self.animals:
            self.animals[name] += mount  # self.animals[name] = self.animals[name] + mount
        else:
            self.animals[name] = mount

    def get_info(self):
        result = f'{self.name}\'s farm'

        # for key, value in self.animals.items():

        for key in self.animals:
            result += f"{key}: {self.animals[key]}\n"

        result += "\tE-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        print(f'{self.name}\'s farm has {",".join(self.get_animal_types())}.')


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()
