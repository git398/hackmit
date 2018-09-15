import random


class StringGenerator:

    def generate_string(self):
        random_length = random.randint(1, 1000000000)
        bits = random.getrandbits(random_length)
        