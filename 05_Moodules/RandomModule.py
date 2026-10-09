# Random Module
import random


# random()
number = random.random()
print("Random float:", number)


# randint()
number = random.randint(1, 10)
print("Random integer:", number)


# randrange()
number = random.randrange(1, 10)
print("Random range value:", number)


# choice()
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruit = random.choice(fruits)
print("Random fruit:", fruit)


# choices()
selected = random.choices(fruits, k=2)
print("Random choices:", selected)


# sample()
numbers = [1, 2, 3, 4, 5]

selected = random.sample(numbers, 3)
print("Random sample:", selected)


# shuffle()
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)
print("Shuffled list:", numbers)


# uniform()
number = random.uniform(1, 10)
print("Random float between 1 and 10:", number)


# seed()
random.seed(10)
print("Seeded random number:", random.randint(1, 100))