# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lboukrou <lboukrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 13:38:34 by lboukrou          #+#    #+#              #
#    Updated: 2020/03/12 18:51:07 by lboukrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# http://sametmax.com/les-context-managers-et-le-mot-cle-with-en-python/
# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/3-further/2-context-managers/

class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file=None
        self.data = []
        self.head=None
        pass

    def __enter__(self):
        print("Enter")
        try:
            self.file = open(self.filename)
            if (self.header == True):
                self.head = self.file.readline()
            for i in range (0, self.skip_top - 1):
                self.file.readline()
            with open(self.filename) as my_file:
                lines_count = (sum(1 for _ in my_file))
            length = 0
            for i in range (self.skip_top, lines_count - self.skip_bottom):
                line = list(filter(None, self.file.readline().strip().split(self.sep)))
                if length == 0:
                    length = len(line)
                assert length == len(line)
                print(line)
                self.data.append(line)
        except:
            print("Error")
            return (None)
        return (self)

    def __exit__(self, type, value, traceback):
        print("Close")
        self.file.close()
    
    def getdata(self):
        return(self.data)
    
    def getheader(self):
        return (self.head)

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        print("toto")
        data = file.getdata()
        header = file.getheader()
        # print(data)
        # print(header)

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
