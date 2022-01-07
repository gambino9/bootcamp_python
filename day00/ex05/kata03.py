# https://thispointer.com/python-how-to-pad-strings-with-zero-space-or-some-other-character/

phrase = "The right format"
padding_size = 42
res = phrase.rjust(padding_size - 1, '-')
print(res)
