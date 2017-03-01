import string
import random
from collections import Counter
from encryptor import Encryptor


class Substitution(Encryptor):

    def __init__(self, word):
        super(Substitution, self).__init__(word)
        # self.ciphr = [random.choice(string.ascii_lowercase + string.digits) for k in range(len(self.alphabet))]
        self.ciphr = list('9fvawbcprd4m5t6lzs32ojkgu')
        print len(self.ciphr)
        print len(set(self.ciphr))

    def _encrypt(self):
        return ''.join([self.ciphr[self.alphabet.index(symb)] for symb in self.word])

    def _decrypt(self):
        return ''.join([self.alphabet[self.ciphr.index(symb)] for symb in self.word])

    def frequency_analysis(self):
        counter = Counter(list(self.word))
        print counter
