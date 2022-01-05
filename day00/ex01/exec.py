# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 18:02:31 by lboukrou          #+#    #+#              #
#    Updated: 2020/01/13 19:38:58 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def rev_alpha(*args):
    phrase = ""
    for arg in args:
        phrase += " ".join(arg)
    res = phrase.swapcase()
    return res[::-1]


if __name__ == "__main__":
    print(rev_alpha(sys.argv[1:]))
