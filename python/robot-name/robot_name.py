import random


def random_letter():
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def random_digit():
    return str(random.randint(0, 9))


def generate_random_name():
    return (
        random_letter()
        + random_letter()
        + random_digit()
        + random_digit()
        + random_digit()
    )


class Robot:
    def __init__(self):
        self.name = generate_random_name()

    def reset(self):
        old_name = self.name

        while old_name == self.name:
            self.name = generate_random_name()
