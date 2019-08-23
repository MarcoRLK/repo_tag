from django.shortcuts import render
import requests
import json

api_token = 'd0ed069c3454b843c2fd'

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
			'User-Agent': 'Python Student',
			'Accept': 'application/vnd.github.v3+json'}

def home(request):

	repo_list = get_repos('marcorlk')

	if repo_list is not None:
		for repo in repo_list:
			print('======================================================')
			print(repo['name'])
	else:
		print('No Repo List Found')

	return render(request, 'index.html')

def get_repos(username):

    api_url = '{}users/{}/repos'.format(api_url_base, username)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None