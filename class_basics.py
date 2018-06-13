# class_basic.py



class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18


class Person2:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name):
        if title not in self.TITLES:
            raise ValueError("%s is invalid." % title)
        self.title = title
        self.name = name


class Person3:

    ALL_TITLES = []
    school = 'UR'

    def __init__(self, title, name):
        if title not in self.ALL_TITLES:
            Person3.ALL_TITLES.append(title)
        self.title = title
        self.name = name

class Person4:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): # instance method
        # instance object accessible through self
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
        # no parameter for class or instance object
        # we have to use ClassName directly
        return [t for t in Person4.TITLES if t.endswith(endswith)]


def test_person1():
    print('\n----Testing Person1----')

    # initiate an instance of Person1
    p1 = Person1('Tom', 23)

    # access instance variables 'name' and 'age'
    print(p1.name)
    print(p1.age)

    # access instance method 'is_adult'
    print(p1.is_adult())


def test_person2():
    print('\n----Testing Person2----')
    p1 = Person2('Mr', 'Tom')
    print(p1.name)

    # test that an exception will be raised
    try:
        p2 = Person2('Mrss', 'Kate')
    except ValueError:
        print('ValueError as expected')

def test_person3():
    print('\n----Testing Person3----')
    p1 = Person3('Mr', 'Tom')
    print(p1.name)

    p2 = Person3('Mrs', 'Kate')

    # access class variable from instance, or from class name, they're shared across all instances
    print(p1.ALL_TITLES)
    print(p2.ALL_TITLES)
    print(Person3.ALL_TITLES)

    # class variable: advanced, for all code below in 'test_person3'
    # since it's shared, if class var is mutable, change in one place, will change in all places
    p1.ALL_TITLES.clear()
    print(p1.ALL_TITLES)
    print(p2.ALL_TITLES)
    print(Person3.ALL_TITLES)

    # if class var is not mutable, then changing instance.class_var will not change class var on other places
    # this is tricky
    print()
    print(p1.school)
    p1.school = 'RIT'
    print(p1.school)
    print(p2.school)
    print(Person3.school)

    # if class var is not mutable, then changing ClassName.class_var may change other instance.class_var
    # this is tricky
    print()
    Person3.school = 'Harvard'
    print(p1.school)
    print(p2.school)
    print(Person3.school)


def test_person4():
    print('\n----Testing Person4----')
    jane = Person4("Jane", "Smith")

    print(jane.fullname())

    # class method, static method: advanced
    print(jane.allowed_titles_starting_with("M"))
    print(Person4.allowed_titles_starting_with("M"))

    print(jane.allowed_titles_ending_with("s"))
    print(Person4.allowed_titles_ending_with("s"))


if __name__ == '__main__':
    test_person1()
    test_person2()
    test_person3()
    test_person4()

