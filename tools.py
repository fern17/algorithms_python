from random import randint
import random


def rand_vector(n, lower, upper):
    ll = [randint(lower,upper) for x in range(1, n)]
    return ll


def rand_vector_f(n, lower, upper):
    ll = [random.uniform(lower, upper) for x in range(1, n)]
    return ll
