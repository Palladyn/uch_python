class Thing:
    pass

class Inanimate(Thing):
    pass

class Animate(Thing):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print("дышать")
    def move(self):
        print("идет")
    def eat_food(self):
        print("есть")

class Mammals(Animals):
    def feed_young_with_milk(self):
        print("кормит молоком")

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print("ест листья")
    def find_food(self):
        self.move()
        print("Найдена еда")
        self.eat_food()
    def left_foot_forward(self):
        print("Левая нога  вперед")
    def left_foot_back(self):
        print("Левая нога  назад")
    def right_foot_forward(self):
        print("Правая нога  вперед")
    def right_foot_back(self):
        print("Правая нога  назад")
    def dance(self):
        self.left_foot_back()
        self.left_foot_forward()
        self.right_foot_back()
        self.right_foot_forward()

#reginald=Giraffes()
#reginald.move()
#reginald.eat_food()


#herold=Giraffes()
#herold.move()


#petro=Giraffes()
#petro.find_food()

kolya=Giraffes()
kolya.dance()