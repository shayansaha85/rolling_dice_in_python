import sys
import random
sys.path.append('.\\dice.py')

from dice import *

while True:
    roll=random.randint(1,6)

    if roll==1:
        one()
    elif roll==2:
        two()
    elif roll==3:
        three()
    elif roll==4:
        four()
    elif roll==5:
        five()
    elif roll==6:
        six()
    input('Press ENTER to roll again')