# -*- coding: utf-8 -*-
import string


class Encryptor(object):

    def __init__(self, word, key=None):
        self.alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'.decode('utf-8'))
        word = ''.join(symb for symb in list(word) if all([symb not in string.punctuation, symb != ' ']))
        self.word = (word.decode('utf-8').lower())
        self.key = key if type(key) == int else key.decode('utf-8')

    def _encrypt(self):
        raise NotImplementedError

    def _decrypt(self):
        raise NotImplementedError
