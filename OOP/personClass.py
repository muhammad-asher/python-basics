class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi , I am {self.name}")


personObj = Person("John Smith")
personObj.talk()

bob = Person("Bob")
bob.talk()