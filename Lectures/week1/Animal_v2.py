class Animal():
    ''' This class defines an animal'''

    def __init__(self, name, classification, animal_type):
        '''(Animal, str, str, str) -> NoneType
        construct a new animal by initializing its attributes.
        REQ: classification is either "vertebrate" or "invertebrate"
        animal_type is either "wild" or "domestic"'''

        # initializing the attributes (instance variables)
        self._animal_attributes = []
        self._animal_attributes.append(name)
        self._animal_attributes.append(classification)
        self._animal_attributes.append(animal_type)

    def get_name(self):
        ''' (Animal) -> str
        return the value of the name
        '''
        return self._animal_attributes[0]

    def get_classification(self):
        ''' (Animal) -> str
        returns the vlaue of this animal's classification'''

        return self._animal_attributes[1]

    def get_animal_type(self):
        '''(Animal) -> str
        returns the value of this animal's type'''
        return self._animal_attributes[2]

    def set_name(self, new_name):
        ''' (Animal, str) -> NoneType
        set a new name for this animal'''

        self._animal_attributes[0] = new_name

    def set_classification(self, new_class):
        '''(Animal, str) -> NoneType
        set a new classification for this animal'''

        self._animal_attributes[1] = new_class

    def set_animal_type(self, new_animal_type):
        '''(Animal, str) -> NoneType
        set a new type for this animal'''

        self._animal_attributes[2] = new_animal_type

    def eat(self):
        print("This animal eats something!")

    def roam(self):
        print("This animal roams wherever it likes!")