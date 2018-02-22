from random import randint
from itertools import combinations, imap, ifilter



def create_rand_list():
	ints = []
	for _ in range(30):
		ints.append(randint(-30,30))
	return ints


def create_triplets_comb(list):
	return [ combo for combo in combinations(list, 3) ]


def main():

	#list of ints
	ints = create_rand_list()
	#iter of triplets
	triplets = create_triplets_comb(ints)
	# We need iterators so keep them.
	sums = list(imap(sum, triplets))
	# Convert them to list, in order to have access to their index.
	triplets = list(triplets)
	for idx, val in enumerate(sums):
		if val == 0:
			print 'The sum of numbers {0} is zero! Hooray !'.format(triplets[idx])
		
		#print num

if __name__ == "__main__":
	main()
