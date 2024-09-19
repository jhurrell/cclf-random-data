import random

c = "123456789"
n = "0123456789"
an = "AN"
a = "ACDEFGHJKMNPQRTUVWXY"

def generate_mbi():
    return f"{random.choice(c)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(a)}{random.choice(n)}{random.choice(n)}"

def generate_mbis(quantity):
    mbis = []

    for _ in range(quantity):
        mbis.append(generate_mbi())

    return mbis

list = generate_mbis(100)
print(list)
