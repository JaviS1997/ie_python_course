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
    result = np.pi * radius ** 2
    print("Surface = π * {}^2 = {}".format(radius, round(result, 2)))
    return 1


def maze():
    moves = 0
    answer = ''
    solution = 'SSNWES'
    print("You are in the magic maze")
    while answer != solution:
        print("Which way to go now ? (N,S,E,W)")
        key = input().upper()
        if key in ['S', 'N', 'E', 'W']:

            answer += key
            if answer == solution[0:moves + 1]:
                moves += 1
                print("Correct! {} move(s) to finish".format(len(solution) - moves))
            else:
                print('Wrong way ! You are going back to the beginning')
                answer = ''
                moves = 0
        else:
            print('Input a correct direction!')

    return print("Congrats! You finished the maze")


def substr():
    print('Input the word whose substring we will use :')
    word = input()
    prior = word[0]
    substring = ''
    longest_substring = ''
    for c in word:
        if c >= prior:
            substring += c
        else:
            if len(substring) >= len(longest_substring):
                longest_substring = substring
            substring = '' + c
        prior = c
    print('The longest alphabetical substring is \'{}\''.format(longest_substring))


# askName()
# division()
# surfaceCircle()
# maze()
substr()
