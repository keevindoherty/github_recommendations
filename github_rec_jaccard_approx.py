from github import Github
import getpass
import operator
import math

import urlparse, requests
from bs4 import BeautifulSoup


username = raw_input("Enter your username: \n")
password = getpass.getpass("Enter your password: \n")
g = Github(username, password)

print g.get_rate_limit().rate.remaining

me = g.get_user()

print me.login

my_likes = set([st for st in me.get_starred()])# | set([wa for wa in me.get_watched()])

print "Getting stargazers and computing similarity"
user_similarity = {}
for repo in my_likes:
	repo_star_count = repo.stargazers_count
	stargazers = set(s.login for s in repo.get_stargazers())
	#subscribers = set(w.login for w in repo.get_subscribers())

	likes = stargazers# | subscribers
	for name in likes:
		if user_similarity.get(name):
			user_similarity[name] = user_similarity[name] + 1
		else:
			user_similarity[name] = 1

star_len = len(user_similarity)
print "Got stargazers, length: ", star_len

if user_similarity.get(username):
	del user_similarity[username]

session = requests.session()
count = 0
for k,v in user_similarity.iteritems():
	if v < 3:
		user_similarity[k] = 0
		count = count + 1
	else:
		user_url = "https://github.com/%s/" % k
		user_page = session.get(user_url)
		user_soup = BeautifulSoup(user_page.text)
		for an in user_soup.findAll('a', {'href': '/stars/%s' % k}):
			for num in an.findAll('strong'):
				num_text = num.text
				if 'k' in num_text:
					num_text = num_text.replace('k', '')
					penalty = float(num_text)*1000.0
				else:
					penalty = float(num_text)
		#print penalty
		user_similarity[k] = v/penalty


print "Number with less than 3 in common: ", count
print "Number left: ", star_len - count
top10 = sorted(user_similarity.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
print top10
