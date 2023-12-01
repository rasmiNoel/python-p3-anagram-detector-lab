class Anagram (object):
    def __init__(self, word):
        self.word = word
        self.letters = sorted(word.lower())
    def match(self, words):
        return [w for w in words if self.is_anagram(w)]
    def is_anagram(self, word):
        return self.letters == sorted(word.lower()) and self.word.lower() != word.lower()