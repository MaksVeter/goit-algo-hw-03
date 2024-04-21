import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    res = []
    # check input types
    if (type(min) == type(max) == type(quantity) == int):
        #check inputs criterias
        if (min < max and min >= 1 and max <= 1000 and \
            quantity > min and quantity < max and quantity <= (max-min+1)):
            res = random.sample(range(min, max+1), quantity)
            res.sort()
            pass

    return res