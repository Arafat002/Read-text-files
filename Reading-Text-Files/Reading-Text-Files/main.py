# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string


def read_file_content(filename):
    f = open(filename, 'r')
    read_file = f.read()
    f.close()
    return (read_file)

    # [assignment] Add your code here 
    



def count_words(line):
    fname = "./story.txt"
    hand = open(fname)

    di = dict()
    for lin in hand:
        lin = lin.rstrip()
        wds = lin.split()
        for w in wds:
            if w in di:
                di[w] = di[w] + 1
            else:
                di[w] = 1
            print(di[w])
    print(di)
