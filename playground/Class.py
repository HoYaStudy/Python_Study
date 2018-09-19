###############################################################################
# @brief    Python3 - Class.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.10 - Created.
###############################################################################

'''
__eq__(self, other)     self == other
__ne__(self, other)     self != other
__lt__(self, other)     self < other
__gt__(self, other)     self > other
__le__(self, other)     self <= other
__ge__(self, other)     self >= other

__add__(self, other)        self + other
__sub__(self, other)        self - other
__mul__(self, other)        self * other
__floordiv__(self, other)   self // other
__truediv__(self, other)    self / other
__mod__(self, other)        self % other
__pow__(self, other)        self ** other

__str__(self)       str(self)
__repr__(self)      repr(self)
__len__(self)       len(self)
'''


class Person():
    count = 0

    # Constructor
    def __init__(self, _name):
        self.__name = _name
        Person.count += 1

    @classmethod
    def population(cls):
        print("There is", cls.count, "peoples.")

    @staticmethod
    def static():
        print("This is a static method.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name

    def say(self):
        print(self.name + ': Hello')


class DerivedPerson(Person):
    def __init__(self, _name, _age):
        super().__init__(_name)
        self.age = _age

    def say(self):
        print(self.name + ': Nice to meet you')

    def sayAge(self):
        print(self.name + ": I'm " + str(self.age) + " years old.")


if __name__ == '__main__':
    print("### Class Study ###")

    # Create Instance
    man1 = Person('HoYa')
    print(man1.name)
    man1.name = 'ChameleoN'
    print(man1.name)
    man1.say()
    man2 = DerivedPerson('Chris', 17)
    man2.say()
    man2.sayAge()
    Person.population()
    Person.static()
