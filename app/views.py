from django.shortcuts import render
import requests
import json
from .models import User, Repository, Tag
from django.http import HttpResponse, HttpResponseRedirect

api_token = 'd0ed069c3454b843c2fd' ## client id

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
			'User-Agent': 'Python Student',
			'Accept': 'application/vnd.github.v3+json'}
            
def show_dashboard(request):

    username = None
    if request.user.is_authenticated:
        username = request.user.username
	
    if request.method == "GET":
        repo_list = get_repos(username)
        return render(request, 'dashboard.html', {'repos': repo_list})
    
    elif request.method == "POST":
        return HttpResponseRedirect('/')

def show_repo(request, github_id):

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    creator = User.objects.get(user_name=username)
    tags = Tag.objects.filter(creator=creator)
    rep = Repository.objects.get(github_id=github_id)

    if request.method == "GET":
        repos = get_repos(username)
        t_repo = [repo for repo in repos if repo['id'] == github_id][0]

        return render(request, 'repository.html', {'repo': t_repo, 'tags' : tags})

    elif request.method == "POST":
        if 'form1' in request.POST:
            boxes = request.POST.getlist("tag_box", None)
            boxes = [int(i) for i in boxes]
            ## atrelar tag ao repo
            print(boxes)
            for t in tags:
                if t.id in boxes:
                    t.repos.add(rep)
                else:
                    t.repos.remove(rep)

        elif "form2" in request.POST:
            tag_name = request.POST['tag_name']
            color = request.POST['color']
            create_tag(tag_name, color, creator)
        return HttpResponseRedirect('/app/repo/' + str(github_id))

def get_repos(username):

    api_url = '{}users/{}/repos'.format(api_url_base, username)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def create_tag(tag_name, color, user):
    new_tag = Tag(tag_name=tag_name, color=color, creator=user)
    new_tag.save()
