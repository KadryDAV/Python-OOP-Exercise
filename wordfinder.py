"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
  
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.read_file(file_path)
        print(f"{len(self.words)} words read")
    
    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return [word.strip() for word in file]
    
    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def parse(self, file_path):
        return [word.strip() for word in file_path if word.strip() and not word.startswith("#")]    