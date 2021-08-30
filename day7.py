class Animal:
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body"

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def make_noise(self):
        return self.noise


class Dog(Animal):
    name = 'Jon'


jon = Dog()
jon.color = 'White'
jon.name = 'Jon Snow'
jon.noise = 'gaw gaw'

jon.get_color()
print(jon.make_noise())
