# objects.. classes

class Car(object):
    def __init__(self):
        self.color = 'blue'


class Honda(Car):

    family = 'car' # attribute

    def __init__(self, age, color, rims = True):
        self.color = color
        self.rims = rims
        self.age = age # attribute

    def get_age(self):
        return self.age

car = Car()
civic = Honda(color = 'green', age = 12) # order doesn't matter

print car.color
print civic.color
print civic.age
print civic.family
print civic.rims
print civic.get_age()

l = range(0, 3)


def fn():
    return ''


print type(1)
print type(l)
print type(True)
print type((1, 2))
print type({'name': 'phil'})
print type(set([1, 2, 3, 4, 4]))
print type(fn)
print type(Car)
print type(Car.__init__)
print type(car)


