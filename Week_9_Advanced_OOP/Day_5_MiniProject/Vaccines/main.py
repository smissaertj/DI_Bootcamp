class Human():
    def __init__(self, id, name, age, priority, blood_type, family=[]):
        self.id = id
        self.name = name
        self.age = age
        self.priority = bool(priority)
        self.blood_type = blood_type
        self.family = family

    def add_family_member(self, person):
        self.family.append(person)


class Queue():
    def __init__(self):
        self.humans = []

    def __str__(self):
        return 'Current Queue:\n'+ ', '.join([str(x.name) for x in self.humans])

    def add_person(self, person):
        self.humans.append(person)

    def find_in_queue(self, person):
        return self.humans.index(person)

    def swap(self, person1, person2):
        index_person1 = self.humans.index(person1)
        index_person2 = self.humans.index(person2)

        temp_1 = self.humans[index_person1]
        temp_2 = self.humans[index_person2]

        self.humans[index_person1] = temp_2
        self.humans[index_person2] = temp_1

    def get_next(self):
        next =  self.humans[0]
        self.humans.remove(next)
        return next

    def get_next_blood_type(self, blood_type):
        next = None
        for human in self.humans:
            if human.blood_type == blood_type:
                next = human
        self.humans.remove(next)
        return next

    def sort_by_age(self):

        ##  Handle and Sort Priority ##
        # Create list of humans with Priority
        priority_list = [x for x in self.humans if x.priority]

        # Sort the priority queue by age descending
        priority_list.sort(key=lambda x:x.age, reverse=True)

        # Remove the humans in the priority queue from the existing list
        self.humans = [x for x in self.humans if x not in priority_list]

        ## Handle and Sort Older people ##
        old_list = [x for x in self.humans if x.age >= 60]
        old_list.sort(key=lambda x:x.age, reverse=True)
        self.humans = [x for x in self.humans if x not in old_list]

        ## Handle and sort younger people
        young_list = [x for x in self.humans if x.age < 60]
        young_list.sort(key=lambda x:x.age, reverse=True)
        self.humans = [x for x in self.humans if x not in young_list]


        # self.humans should now be empty, let's rebuild it properly sorted: priority_list > old_list > young_list:
        list(map(lambda x: self.humans.append(x), priority_list))
        list(map(lambda x: self.humans.append(x), old_list))
        list(map(lambda x: self.humans.append(x), young_list))

    def rearange_queue(self):
        for human in self.humans:
            if human in self.humans[self.humans.index(human) + 1]:
                self.swap(human, self.humans[self.humans.index(human) + 3])



person1 = Human('1', 'person1', 35, True, 'A')
person2 = Human('2', 'person2', 60, False, 'B')
person3 = Human('3', 'person3', 80, True, 'B')
person4 = Human('4', 'person4', 80, False, 'B')
person5 = Human('5', 'person5', 35, True, 'A')
person6 = Human('6', 'person6', 35, False, 'A')

my_queue = Queue()

my_queue.add_person(person1)
my_queue.add_person(person2)
my_queue.add_person(person3)
my_queue.add_person(person4)
my_queue.add_person(person5)
my_queue.add_person(person6)

my_queue.sort_by_age()
print(str(my_queue))

my_queue.get_next()
my_queue.get_next_blood_type('A')

print(str(my_queue))