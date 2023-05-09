import random
import string

def generate_password(length):
    # Lowercase, uppercase and numbers
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for i in range(length))

    return password

password = generate_password((10))
print(password)

