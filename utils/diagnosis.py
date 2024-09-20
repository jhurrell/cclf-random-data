import random
import functools
from faker import Faker

# Cache the results of the generate_mbis function to improve performance and to
# support sharing the same generated MBIs across multiple calls to the function.
@functools.lru_cache(maxsize=None)  # maxsize=None means unlimited cache
def generate_diagnoses(quantity):
    codes = []
    for _ in range(quantity):

        category = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        code = category + str(random.randint(1, 99)) + '.' + str(random.randint(1, 999))
        
        codes.append({
            "code": code,
            "ver": random.choice(["0", "9", "U"])
        })

    return codes
