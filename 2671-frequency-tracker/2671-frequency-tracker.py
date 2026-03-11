from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)   # number -> frequency
        self.freq = defaultdict(int)    # frequency -> how many numbers have this frequency

    def add(self, number: int) -> None:
        old_freq = self.count[number]
        new_freq = old_freq + 1
        
        self.count[number] = new_freq
        
        if old_freq > 0:
            self.freq[old_freq] -= 1
        
        self.freq[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.count[number]
        
        if old_freq == 0:
            return
        
        new_freq = old_freq - 1
        self.count[number] = new_freq
        
        self.freq[old_freq] -= 1
        
        if new_freq > 0:
            self.freq[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
