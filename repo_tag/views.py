from django.shortcuts import render
import requests
import json
from app.models import User, Repository

api_token = 'd0ed069c3454b843c2fd' ## client id

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
			'User-Agent': 'Python Student',
			'Accept': 'application/vnd.github.v3+json'}

def home(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.username
		
		save_user_repos(username)

	return render(request, 'index.html', {})

def get_repos(username):

    api_url = '{}users/{}/repos'.format(api_url_base, username)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def save_user_repos(username):
	try:
		user = User.objects.get(user_name=username)
	except User.DoesNotExist:
		user = User(user_name=username)
		user.save()
	
	repos = get_repos(username)

	for repo in repos:
		try:
			n_repo = Repository.objects.get(github_id=repo['id'])
		except Repository.DoesNotExist:
			n_repo = Repository(github_id=repo['id'], owner=user)
			n_repo.save()