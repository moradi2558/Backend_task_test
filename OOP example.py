class Animal:
    def speak(self):
        print('animal sound')
    
class Dog(Animal):
    def speak(self):
        print('Hop Hop')


dog = Dog()
dog.speak()