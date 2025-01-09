import random
import string

def generate_password(length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(elements) for _ in range(length))
    return password