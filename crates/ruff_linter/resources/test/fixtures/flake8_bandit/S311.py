import os
import random

import a_lib
import secrets

# OK
random.SystemRandom()

# Errors
secrets.SystemRandom().Random()
secrets.SystemRandom().random()
secrets.SystemRandom().randrange()
secrets.SystemRandom().randint()
secrets.choice()
secrets.SystemRandom().choices()
secrets.SystemRandom().uniform()
secrets.SystemRandom().triangular()
secrets.SystemRandom().randbytes()

# Unrelated
os.urandom()
a_lib.random()
