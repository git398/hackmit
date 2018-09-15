import random
import sys

# random ints and floats

def gen_int():
    return random.randint(-(sys.maxsize), sys.maxsize)
def gen_float():
    #print(type(sys.maxsize * 1.0))
    return random.randrange(-(sys.maxsize * 1.0), sys.maxsize * 1.0)

if __name__ == '__main__':
    print("exec")
    print(gen_float())
