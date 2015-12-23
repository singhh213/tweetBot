import tweepy, time, sys

CONSUMER_KEY = '0kHfG8Qr27e8DQl7UEorNXnBv'
CONSUMER_SECRET = 'uvdD0EKE6PmATnhZUnqgzbsPR3udgNq0H47yNGtfSAa7JJgRSj'
ACCESS_KEY = '907269530-gJgJTQh6EYSUiLeFBwDXkSss92mIxMflDY8sHH5y'
ACCESS_SECRET = 'ujyFT4VYlCEio72sv9bE2tGVMEQnh96IayqODU403whxq'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

filename = "tweets.txt"

try:
	with open(filename, 'r') as tweetfile:
			f = tweetfile.readlines()

	for line in f[:]:
		with open(argfile, 'w') as tweetfile:
			f.remove(line)
			tweetfile.writelines(f)
		line = line.strip(' \n');
		if len(line) <= 140 and len(line) > 0:
			print("Tweeting...")
			twitter.update_status(status=line)
			print("successful!")
			time.sleep(30)
		else:
			print("Skipped line - length violation. Has to be within 1-140 chars long")
			continue
	print("No more lines to tweet")

except tweepy.TweepError as e:
	print(e)


def getTrends():
	trends = twitter.trends_place(1)[0]['trends']
	names = [trend['name'] for trend in trends]
	for name in names:
		print(name)

def searchTweets(keyword):
	search = twitter.search(q=keyword, count=10)
	for result in search:
		print result.text
