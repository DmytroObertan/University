import string


class Encryptor(object):

    def __init__(self, word, key=None):
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')
        word = ''.join(symb for symb in list(word) if all([symb not in string.punctuation, symb != ' ']))
        self.word = word.lower()
        self.key = key

    def _encrypt(self):
        raise NotImplementedError

    def _decrypt(self):
        raise NotImplementedError
