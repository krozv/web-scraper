class Puppy:
    
    def __init__(self, name, breed) -> None:
        self.name = name
        self.age = 0.1
        self.breed = breed
    
    def __str__(self) -> str:
        return f'Puppy name is {self.name}.'

happy = Puppy('happy', 'beagle') # Puppy의 종류인 happy (instance 생성)
choco = Puppy('choco', 'dalmatian')

print(happy, choco)
# print(happy.name, happy.breed)