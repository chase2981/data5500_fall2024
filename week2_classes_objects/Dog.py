class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return "This dog is " + self.age + " years old"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_color(self):
        return self.color
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_color(self, color):
        self.color = color

best_dog_ever = Dog('turbo', 15, 'brown')

print(best_dog_ever)

other_dog = Dog('other', 2, 'white')

print(other_dog)
