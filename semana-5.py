class Apple:
    color = ""
    flavor = ""
jonagold = Apple ()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print (jonagold.color.upper())
golden = Apple()
golden.color = "Yellow"
golden.flavor = "soft"

#classes and methods
class piglet:
    def speak(self):
        print("oink oink")

hamlet = piglet()
hamlet.speak()

class piglet:
    name = "piglet"
    def speak(self):
        print("oink ! I`m {} ! oink!".format(self.name))

hamlet = piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = piglet()
petunia.name = "Petunia"
petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor  is  {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)

"""help(Apple)"""

class Piglet:
    """Represents a piglet that can say their name"""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet. """
        print("oink ! I`m {} ! oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to qequivalent pig years."""
        return self.years * 18
#Code Reuse

class Animal:
    sound = ""
    def __init__(self, name):
        self.name  = name 
    def speak(self):
        print("{sound} I`m {name}! {sound}".format(
            name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()
class Cow(Animal):
    sound = "moooo"

milky = Cow("milky, white")
milky.speak()

class Repository:
    def __init__(self):
        self.packages = {}
    def add_packages(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result
