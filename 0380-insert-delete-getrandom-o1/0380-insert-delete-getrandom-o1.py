import random
class RandomizedSet:

    def __init__(self):
        self.container = set()

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        else:
            self.container.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.container:
            self.container.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(tuple(self.container))

        

