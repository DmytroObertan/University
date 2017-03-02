# -*- coding: utf-8 -*-
from collections import Counter, OrderedDict
from encryptor import Encryptor


class Substitution(Encryptor):

    def __init__(self, word):
        super(Substitution, self).__init__(word)
        self.ciphr = list('йцукенгшщґзхїфівапролджєячсмитьбю'.decode('utf-8'))

    def _encrypt(self):
        return ''.join([self.ciphr[self.alphabet.index(symb)] for symb in self.word])

    def _decrypt(self):
        return ''.join([self.alphabet[self.ciphr.index(symb)] for symb in self.word])

    def frequency_analysis(self):
        counter = Counter(list(self.word))
        coun = OrderedDict(counter)
        frequency = list('оанвиіетклрсудмпбгзяєжїйхцчшщьюфґ'.decode('utf-8'))
        for key, freq in zip(coun, frequency):
            new = self.word.replace(key, freq)
            self.word = new
        return self.word
