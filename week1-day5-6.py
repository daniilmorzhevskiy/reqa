#08.10.2026

#Classses and objects

class OopsException(Exception):
    def __init__(self):
        print("Oops! Something went wrong.")


words = ['cat', 'window', 'defenestrate', 'MO']

for word in words:
    if word == 'MO':
        raise OopsException


class Cat:
    pass

a_cat = Cat()
another_cat = Cat()

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat

class Cat:
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')
print('Our latest addition: ', furball.name)


class Car:
    pass
     
class Yugo(Car):
    pass
     
issubclass(Yugo, Car)

give_me_a_car = Car()
give_me_a_yugo = Yugo()
 
class Car():
    def exclaim(self):
        print("I`m a Car!")
         
class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

