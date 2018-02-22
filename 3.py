import argparse
import os  

def parse_args():
	parser = argparse.ArgumentParser(description='Read text from a file and encode it with rot13.')
	parser.add_argument('--file', '-f', dest='file', required=True, help='File to be read')
	return parser.parse_args()


def rot13(txt):
	def rot13_char(v):
	    o, c = ord(v), v.lower()
	    if 'a' <= c <= 'm':
	        return chr(o + 13)
	    if 'n' <= c <= 'z':
	        return chr(o - 13)
	    return v
	return ''.join(map(rot13_char, txt))


def main():

	args = parse_args()
	if os.path.isfile(args.file):
		with open(args.file, 'r') as f:
			text = f.read()
			if text:
				rot13_txt = rot13(text)
				with open('rot13_text.txt','w') as nf:
					nf.write(rot13_txt)
				nf.close()
		f.close()


if __name__ == "__main__":
    main()