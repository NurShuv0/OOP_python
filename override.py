class person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("person eats")
    def sleep(self):
        print("person sleeps")

class cricketer(person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print("player eats")

per_obj = person("nur",22, 69, 65)
per_obj.eat()

crick_obj = cricketer("nur_player", 22, 55, 77, "BD")
crick_obj.eat()
