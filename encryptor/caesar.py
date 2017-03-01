from encryptor import Encryptor


class Caesar(Encryptor):

    def __init__(self, word, key):
        super(Caesar, self).__init__(word, key)

    def _encrypt(self):
        new_word = []
        for symb in list(self.word):
            try:
                new_symb = self.alphabet[self.alphabet.index(symb) + self.key]
            except IndexError:
                new_symb = self.alphabet[abs(len(self.alphabet) - self.alphabet.index(symb) - self.key)]
            new_word.append(new_symb)
        return ('').join(new_word)

    def _decrypt(self):
        new_word = []
        for symb in list(self.word):
            try:
                new_symb = self.alphabet[self.alphabet.index(symb) - self.key]
            except IndexError:
                new_symb = self.alphabet[len(self.alphabet) + (self.alphabet.index(symb) - self.key)]
            new_word.append(new_symb)
        return ('').join(new_word)
