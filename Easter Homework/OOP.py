class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

class GoldenRetriever(Dog):
    def eat(self, food):
        return "{} likes to eat {}".format(self.name, food)

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

dog1 = GoldenRetriever("Mai", "8")
print(dog1.description())
print(dog1.eat("salmon"))
print(dog1.speak("grr"))
print(dog1.run("slowly"))
