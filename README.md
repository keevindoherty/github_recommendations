# Github Recommendations
Recommends Github Repos Sometimes

Try out both scripts! They might take a while. This was pretty much catered completely to me, so no guarantees. There is a high probability you will need to make some modifications in order make this work for you. `github_rec_v2.py` worked better for me.

## Getting Started

To install requirements, either set up and activate your virtualenv from the project root with:

```sh
$ virtualenv venv # virtualenv2 if you're on Arch
$ source venv/bin/activate
$ pip install -r requirements.txt
```

And you're good to go. `deactivate` will deactivate the virtualenv.

If you don't like virtualenv or you looked at `requirements.txt` and saw there's only one dependency in there, you can also just run `sudo pip install pygithub` to get the Github API Python wrappers I'm using for this project.