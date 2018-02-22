import argparse
import os
import re
from random import randint
from itertools import izip_longest


#https://stackoverflow.com/questions/434287/what-is-the-most-pythonic-way-to-iterate-over-a-list-in-chunks/434411#434411
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def parse_args():
	parser = argparse.ArgumentParser(description='Read text from a file and construct a new one.')
	parser.add_argument('--file', '-f', dest='file', required=True, help='File to be read')
	return parser.parse_args()


def extract_words(file):
	words_list = []
	with open(file, 'r') as f:
			txt = f.read()
			words_list = re.findall("[a-z]+", txt)
	f.close()
	return words_list


def main():
	args = parse_args()
	if os.path.isfile(args.file):
		words = extract_words(args.file)
		if words:	
			grouped_words = grouper(words, 3, '')
			l = list(grouped_words)
			start_point = randint(0, len(l) - 1)
			for u in grouped_words:
				print u



if __name__ == "__main__":
	main()