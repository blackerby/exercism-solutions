import random
import string

class Robot:
    used_names = []
    
    def __init__(self):
        self.name = self.reset()

    def reset(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        self.name = ''.join(letters + digits)
        if self.name not in self.used_names:
            self.used_names.append(self.name)
            return self.name
        else:
            self.reset()
