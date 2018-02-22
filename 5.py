from TwitterAPI import TwitterAPI
import argparse

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''



def parse_args():
	parser = argparse.ArgumentParser(description='Get the most popular word of the latest 10 tweets.')
	parser.add_argument('--profile', '-pr', dest='pr_name', required=True, help="Twitter's account name without the char @")
	return parser.parse_args()




def get_tweets(name):
	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, auth_type='oAuth1', proxy_url= None)
	json = { "screen_name" : name, "count": 10, "include_rts": False, "exclude_replies": True }
	return api.request('statuses/user_timeline', json)


def tweet_ranking(tweets):

	tweet_dict = dict()
	for twt in tweets:
		txt = twt['text']
		words = txt.split(" ")
		for word in words:
			if word in tweet_dict:
				tweet_dict[word] += 1
			else:
				tweet_dict[word] = 1
	return tweet_dict

def get_most_used(dc):
	idx = 0
	cur = 1
	for key, value in dc.iteritems():
		if value > cur:
			idx = key
			cur = value

	if cur == 1:
		print 'All tweets have unique words.'
	else:
		print u'[*] The most used word in tweets is {0} used {1} times'.format(idx, dc[idx])


def main():

	args = parse_args()
	tweets = get_tweets(args.pr_name)
	if tweets and tweets.status_code == 200:
		tweet_dict = tweet_ranking(tweets)
		get_most_used(tweet_dict)

if __name__ == "__main__":
	main()
