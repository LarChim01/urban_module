class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == True:
            print(f' {self.name}  съел  {food.name} ')
            self.fed = True

        else:
            print(f' {self.name} не стал есть {food.name} ')
            self.fed = False


class Predator(Animal):
    edible = True

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, food):
        if food.edible == True:
            print(f' {self.name}  съел  {food.name} ')


class Flower(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name
        if self.edible == True:
            self.edible = False
        else:
            self.edible = True



if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)