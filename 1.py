"""docstring"""

"""Hello from github"""

"""Hello from Local"""
def main():
    """docstring"""
    allmoney = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    allmoney1 = allmoney - water
    if allmoney1 % 3 == 0:
        allmoney1 -= 10 * snack1
        cast1 = 10 * snack1
    elif allmoney1 % 3 == 1:
        allmoney1 -= 15 * snack1
        cast1 = 15 * snack1
    elif allmoney1 % 3 == 2:
        allmoney1 -= 20 * snack1
        cast1 = 20 * snack1

    if allmoney1 % 3 == 0:
        allmoney1 -= 12 * snack2
        cast2 = 12 * snack2
    elif allmoney1 % 3 == 1:
        allmoney1 -= 15 * snack2
        cast2 = 15 * snack2
    elif allmoney1 % 3 == 2:
        allmoney1 -= 18 * snack2
        cast2 = 18 * snack2

    if allmoney1 % 3 == 0:
        allmoney1 -= 5 * snack3
        cast3 = 5 * snack3
    elif allmoney1 % 3 == 1:
        allmoney1 -= 7 * snack3
        cast3 = 7 * snack3
    elif allmoney1 % 3 == 2:
        allmoney1 -= 9 * snack3
        cast3 = 9 * snack3

    if allmoney1 < 0:
        print("Now you have %d left." % allmoney)
        print("You don't have enough money!")

    else:
        print("Now you have %d left." % allmoney1)
        print("Here's your order!")
        print("Water: %d baht" % water)
        print("Snack number 1: %d baht" % cast1)
        print("Snack number 2: %d baht" % cast2)
        print("Snack number 3: %d baht" % cast3)
main()
