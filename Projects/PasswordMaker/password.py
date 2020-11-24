import random, string
import sys


def password(length, num=False, Strength="weak"):
    """
    Length of password, num if you want a number,
    and strength(weak, strong, very)
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    punct = string.punctuation
    dig = string.digits
    pwd = ""

    if Strength == "weak" or "WEAK" or "Weak":
        if num:
            length -= 3
            for _ in range(3):
                pwd += random.choice(dig)

        for i in range(length):
            pwd += random.choice(lower)

    elif Strength == "Strong":
        if num:
            length -= 2
            for _ in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)

    elif Strength == "Very":
        ran = random.randint(2, 4)
        if num:
            length -= ran
            for _ in range(2):
                pwd += random.choice(dig)
        length -= ran
        for i in range(length):
            pwd += random.choice(punct)

        for i in range(length):
            pwd += random.choice(letter)

    pwd = list(pwd)
    random.shuffle(pwd)

    return "".join(pwd)
