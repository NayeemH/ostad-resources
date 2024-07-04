class Person:
    def __init__(self, s):
        self.name = s

    def hello(self):
        print("Hello", self.name)

t = Person("Mike")
t.hello()

