#5-1 Conditional tests
bike = 'schwinn'
print("is bike == 'schwinn'? I predict True.")
print(bike == 'schwinn')

print("\nIs bike == 'mongoose'? I predict False")
print(bike == 'mongoose')

print("\nIs bike == 'gt'? I predict False")
print(bike == 'gt')

print("\nIs bike == 'rally'? I predict False")
print(bike =='rally')

alien_colors = ['green','yellow','red']

if 'green' in alien_colors:
    print("You earned 5 points!!")
if 'yellow' in alien_colors:
    print("You earned 10 points!!")
if 'red' in alien_colors:
    print("You earned 15 points!!")

if 'yellow'in alien_colors:
    print("You just eanred 10 points!!")
    elif 'green'in alien_colors:
    print("You just earned 5 points")

