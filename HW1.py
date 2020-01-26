import numpy as np

def askName():
    print("What's your name ?")
    name = input()
    print("Nice to meet you {} !".format(name))
    return 1


def division():
    print("Input two integer numbers for the division. \nNumerator :")
    num = int(input())
    print("Denominator :")
    denominator = int(input())
    # Rounded up to one decimal
    print("{} / {} = {}".format(num, denominator, round(num / denominator, 1)))
    return 1


def surfaceCircle():
    print("Radius of the circle :")
    radius = float(input())
    result = np.pi * radius**2
    print("Surface = π * {}^2 = {}".format(radius, round(result, 2)))
    return 1

#askName()
#division()
#surfaceCircle()
