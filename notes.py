# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

#In python to make a class just type in class and put the name of the class in front of it

class Dog:
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favourite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        s = "Dog's name is " + self.name + "\n"
        s += "and age is " + str(self.age) + "\n"
        s += "and fur clor is " + str(self.fur_color) + "\n"
        s += "they have played fetch " + str(self.fetch_count) +"times\n"
        return s

    def play_fetch(self, num_times):
        self.fetch_count += num_times

MrbergDog = Dog("logan","black",7,"salmon")
ChrisDog = Dog("luna","black and white", 6, "tortilla")

print(MrbergDog)
print(ChrisDog)

MrbergDog.play_fetch(20)
ChrisDog.play_fetch(3)

print(MrbergDog)
print(f"{ChrisDog.name} has played fetch {ChrisDog.fetch_count} times")

