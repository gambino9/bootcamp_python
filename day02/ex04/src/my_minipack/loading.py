# https://stackoverflow.com/questions/3160699/python-progress-bar

import time


def ft_progress(lst):
	iteration = 1
	start = time.time()
	bar_len = 20
	total = len(lst)
	for i in lst:
		percent = int(100 * (iteration / float(total)))
		elapsed_time = time.time() - start
		eta = (elapsed_time * total / iteration) - elapsed_time
		filled_len = int(bar_len * iteration // total)
		progression_bar = "=" * filled_len + '>' + ' ' * (bar_len - filled_len)
		print(
			f"\rETA: {eta:4.2f}s [{percent:3}%][{progression_bar}]{iteration}/{total} | elapsed time {elapsed_time:.2f}s",
			end='')
		iteration += 1
		yield i


if __name__ == "__main__":
	# listy = range(1000)
	# ret = 0
	# for elem in ft_progress(listy):
	# 	ret += (elem + 3) % 5
	# 	time.sleep(0.01)
	# print()
	# print(ret)

	# listy = range(3333)
	# ret = 0
	# for elem in ft_progress(listy):
	# 	ret += elem
	# 	time.sleep(0.005)
	# print()
	# print(ret)

	# Test from correction subjects :
	# X = range(100)
	# X = range(100, 200)
	# X = range(1)
	# X = range(4)
	X = range(0, -100, -1)

	ret = 0
	for elem in ft_progress(X):
		ret += (elem + 3) % 5
		time.sleep(0.1)
	print()
	print(ret)
