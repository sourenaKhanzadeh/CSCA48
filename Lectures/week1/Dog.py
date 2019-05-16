from Compsci_II.Lectures.week1.AbstractAnimal import Animal


# replace it with Animal_v1 and Animal_v2 and see the result

class Dog(Animal):
    def __init__(self):
        ''' (Dog) -> NoneType
        initializes the instances variables of this dog'''

        super().__init__("dog", "vertebrate", "domestic")

    def eat(self):
        ''' (Dog) ->NoneType
        overrides the super eat method'''

        print("This is a dog who loves to lick a bone")

    def __str__(self):
        '''(Dog)->str
        returns the attributes of this dog'''
        return "This is a " + Animal.get_animal_type(self) + " " + Animal.get_name(
            self) + ", which is classified as " + Animal.get_classification(self)


if (__name__ == "__main__"):
    my_animal = Dog()
    my_animal.set_animal_type("domestic")
    my_animal.eat()
    my_animal.roam()
    print(my_animal)
    # this only works if you extend AbstractAnimal
    # my_animal.play()

    # This does not work in case you use AbstractAnimal because Aniaml is abstract and is not supposed to be instantiated.
    # your_animal = Animal("Cat", "vertebrate", "Domestic")
    # print(your_animal.get_name())
