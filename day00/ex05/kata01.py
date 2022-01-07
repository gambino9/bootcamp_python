languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}


def kata01(dic):
	for elem in dic:
		print(elem, "was created by", dic[elem])


if __name__ == "__main__":
	kata01(languages)
