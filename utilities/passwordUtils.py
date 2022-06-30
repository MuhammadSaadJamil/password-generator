import string
from random import shuffle, sample, randint

"""Generate a random list of alpha characters of random length
Input: None
Output: list of alphabets
"""


def get_random_alpha_list():
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    shuffle(upper_case)
    shuffle(lower_case)
    data = sample(lower_case * 2, randint(10, 30)) + sample(upper_case * 2, randint(10, 30))
    shuffle(data)
    return data


"""Generate a random list of numerics of random length
Input: None
Output: list of numerics
"""


def get_random_num_list():
    return [str(randint(0, 9)) for i in range(randint(10, 30))]


"""Generate a random list of special characters of random length
Input: None
Output: list of special characters
"""


def get_random_special_character_list():
    data = list(string.punctuation)
    shuffle(data)
    return sample(data, randint(5, 10))


"""Geerate a random password of given length based on user inputs
Inputs: length: length of password, alpha: boolean indicating inclusion of alpha characters,
        num: boolean indicating inclusion of numeric characters,
        special: boolean indicating inclusion of special characters
Output: random password : String
"""


def generate_password(length=20, alpha=True, num=True, special=True):
    data = []
    data += get_random_alpha_list() if alpha else []
    data += get_random_num_list() if num else []
    data += get_random_special_character_list() if special else []
    shuffle(data)
    data *= 10
    if len(data):
        data = sample(data, length)
        return "".join(data)
    return "Please Enable at least one option to generate password.\nOptions:\n\t1.alpha\n\t2.num\n\t3.special"
