class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, word):
		if not isinstance(coefs, list) or not isinstance(word, list):
			return -1
		if len(coefs) != len(word):
			return -1

		return sum([a * len(b) for a, b in zip(coefs, word)])

	@staticmethod
	def enumerate_evaluate(coefs, word):
		if not isinstance(coefs, list) or not isinstance(word, list):
			return -1
		if len(coefs) != len(word):
			return -1

		enum_coefs = list(enumerate(coefs))
		enum_word = list(enumerate(word))

		return sum([enum_coefs[i][1] * len(enum_word[i][1]) for i in range(len(enum_word))])


# if __name__ == "__main__":
# 	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# 	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#
# 	print(Evaluator.zip_evaluate(coefs, words))
# 	print(Evaluator.enumerate_evaluate(coefs, words))
