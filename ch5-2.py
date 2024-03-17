class Dog:
    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

class GuardDog(Dog):

    def grrr_grrr(self):
        print('Grrr Grrr!')

class Puppy(Dog):
    
    def __str__(self) -> str:
        return f'Puppy name is {self.name}.'
    
    def woof_woof(self):
        print('Woof Woof!')


happy = Puppy('happy', 1, 'beagle') # Puppy의 종류인 happy (instance 생성)
choco = Puppy('choco', 1, 'dalmatian')

# print(happy, choco)
# print(happy.name, happy.breed)
happy.woof_woof()
cute = GuardDog('cuty', 3, 'bulldog')
cute.grrr_grrr()