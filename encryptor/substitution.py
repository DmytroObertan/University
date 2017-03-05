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
        new_word = ['' for i in range(len(self.word))]
        self.ciphr = list('оанвиіетклрсудмпбгзяєжїйхцчшщьюфґ'.decode('utf-8'))
        counter = Counter(list(self.word))
        coun = OrderedDict(reversed(sorted(counter.items(), key=lambda x: x[1])))
        self.alphabet = [w for w in coun]
        return self._encrypt()

    @staticmethod
    def repl(word, a, b):
        a = a.decode('utf-8')
        b = b.decode('utf-8')
        word = list(word)
        # new_word = ['' for i in range(len(self.word))]
        for i in range(len(word)):
            if word[i] == a:
                word[i] = b
            elif word[i] == b:
                word[i] = a
        return ''.join(word) 
 