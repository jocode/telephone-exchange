# Import module
import random as r

def get_random_number():
    """
    This function returns a random number between 1 and 10
    """
    # Phone number have a length of 10
    phone_number = []

    # The first number should be a 3
    phone_number.append(3)
    # The second number can be any digit between 0 and 2
    phone_number.append(r.randint(0, 2))

    # To other numbers can be any digit between 0 and 9
    for i in range(8):
        phone_number.append(r.randint(0, 9))

    # Return the phone number
    return ''.join(str(n) for n in phone_number)
