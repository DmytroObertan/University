from encryptor import Encryptor

class Vigener(Encryptor):

	def __init__(self, word, key):
		super(Vigener, self).__init__(word, key)
		new_key = ''
		for i in range(len(self.word) / len(self.key)):
			new_key += self.key
		new_key += self.key[:len(self.word) % len(self.key)]
		self.key = new_key


	def _encrypt(self):
		new_word = []
		for symb, key in zip(self.word, self.key):
			index = (self.alphabet.index(symb) + self.alphabet.index(key)) % len(self.alphabet)
			new_word.append(self.alphabet[index])
		return ''.join(new_word)

	def _decrypt(self):
		new_word = []
		for symb, key in zip(self.word, self.key):
			index = self.alphabet.index(symb) - self.alphabet.index(key)
			index = len(self.alphabet) + index if index < 0 else index
			new_word.append(self.alphabet[index])
		return ''.join(new_word)

