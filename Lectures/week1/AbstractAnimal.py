
from abc import ABC, abstractmethod
# To define an abstract class, your class is required to both inherits from ABC and decorates at least one of its method
# with @abstractmethod decorator


class dangerException(Exception):
    pass


class Animal (ABC):
    # A class representing an animal and throw an exception in case a wild animal is played with.
    def __init__(self, name, classification, animal_type):
        ''' (Animal, str, str, str) -> NoneType
        initializes the attributes of an animal
        REQ: animal_type is either domestic or wild,
        classification is either vertebrate or invertebrate'''
        self._name = name
        self._classification = classification
        self._animal_type = animal_type

    def get_name(self):
        ''' (Animal) -> str
        returns the name of this animal'''
        return self._name

    def get_classification(self):
        ''' (Animal) -> str
        returns the classification of this animal'''
        return self._classification

    def get_animal_type(self):
        ''' (Animal) -> str
        returns the type of this animal'''
        return self._animal_type

    def set_name(self, new_name):
        ''' (Animal, str) -> NoneType
        sets the name of an animal'''
        self._name = new_name

    def set_classification(self, new_class):
        ''' (Animal, str) -> NoneType
        sets the classification of an animal'''
        self._classification = new_class

    def set_animal_type(self, new_type):
        ''' (Animal, str) -> NoneType
        sets the classification of an animal'''
        self._animal_type = new_type

    @abstractmethod
    def eat (self):
        ''' (Animal) -> NoneType
        This is an abstract method that cannot be called except inside the subclass of
        Animal. This method must be overriden in subclasses of Animal'''
        print("This animal eats something!")

    def roam(self):
        ''' (Animal) -> NoneType
        output the way an animal roams'''
        print("This animal roams wherever it likes!")

    def play(self):
        ''' (Animal) -> NoneType
        output the way an animal plays
        Raise an exception if the animal cannot play with human'''
        if (self._animal_type == "domestic"):
            print ( "playing with the " + self._name + "...")
        else:
            raise dangerException


