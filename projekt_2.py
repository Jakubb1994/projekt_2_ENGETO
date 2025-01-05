"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Prajzler
email: prajzler25@gmail.com
"""
import random

def generate_secret_number():
    # Generates a random 4-digit number with unique digits, not starting with 0
    digits = list(range(1, 10))                  # First digit num. cannot be 0
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    other_digits = random.sample(digits + [0], 3)
    return str(first_digit) + ''.join(map(str, other_digits))