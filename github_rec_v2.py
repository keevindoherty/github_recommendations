from github import Github
import getpass
import operator
import math

username = raw_input("Enter your username: \n")
password = getpass.getpass("Enter your password: \n")
g = Github(username, password)

print g.get_rate_limit().rate.remaining

me = g.get_user()

print me.login

my_stars = set(me.get_starred())

user_similarity = {}
for repo in my_stars:
	repo_star_count = repo.stargazers_count
	for s in repo.get_stargazers():
		if user_similarity.get(s.login):
			user_similarity[s.login] = user_similarity[s.login] + 1/math.log(repo_star_count)
		else:
			user_similarity[s.login] = 1/math.log(repo_star_count)

if user_similarity.get(username):
	del user_similarity[username]

top10 = sorted(user_similarity.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
print top10

for top in top10:
	print [rep.full_name for rep in g.get_user(top[0]).get_starred()[:10]]
