import random
def generatepassword(ask):
    password = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    passw = ''

    for i in range(ask):

        generator = random.choice(password)
        passw += generator
    

    return passw