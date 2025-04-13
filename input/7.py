import random
import string

def generate_nitro():
    nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print(f"Voici un code Nitro généré : https://discord.gift/{nitro_code}")

generate_nitro()