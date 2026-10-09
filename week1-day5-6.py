#08.10.2026

#Classses and objects

# class OopsException(Exception):
#     def __init__(self):
#         print("Oops! Something went wrong.")


# words = ['cat', 'window', 'defenestrate', 'MO']

# for word in words:
#     if word == 'MO':
#         raise OopsException


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






class User:
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role

    def can_delete(self):
        return self.role == "admin"

    def __str__(self):
        return f"{self.name} ({self.email})"

admin = User("Daniil", "daniil@example.com", role="admin")
print(admin)
print(admin.can_delete())  # True


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name



class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2