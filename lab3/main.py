#import reverse_polish_notation as rpn
import random

from reverse_polish_notation import *

from monte_carlo import approximate_pi

def main():
    #print(rvp("((2+7)/3+(8-3)*4)/2")) # 2 7 + 3 / 8 3 − 4 * + 2 /
    #print(solve("2 7 + 3 / 14 3 - 4 * + 2 /"))
    print(approximate_pi())


if __name__ == "__main__":
    main()

