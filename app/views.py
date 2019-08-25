from django.shortcuts import render
import requests
import json
from .models import User, Repository, Tag
from django.http import HttpResponse, HttpResponseRedirect

api_token = 'd0ed069c3454b843c2fd' ## client id
api_secret = 'faf64f58ec342492e929d38829596a704e96a4e7'

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
			'User-Agent': 'Python Student',
			'Accept': 'application/vnd.github.v3+json'}
            
def show_dashboard(request):

    username = None
    if request.user.is_authenticated:
        username = request.user.username
	
    repo_list = get_repos(username)
    tag_list = []
    for n in range(len(repo_list)):
        tag_list.append(list(get_repotags(repo_list[n]['id'])))
    
    data = zip(repo_list, tag_list)
    
    return render(request, 'dashboard.html', {'data': data})


def show_repo(request, github_id):

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    creator = User.objects.get(user_name=username)
    tags = Tag.objects.filter(creator=creator)
    bd_rep = Repository.objects.get(github_id=github_id)
    marked_tags = bd_rep.tags.all()

    if request.method == "GET":
        all_repos = get_repos(username)
        repo_by_id = [repo for repo in all_repos if repo['id'] == github_id][0]

        return render(request, 'repository.html', {'repo': repo_by_id, 'tags' : tags,
                                                    'marked_tags': marked_tags})

    elif request.method == "POST":
        if 'form1' in request.POST:
            boxes = request.POST.getlist("tag_box", None)
            boxes = [int(i) for i in boxes]
            ## atrelar tag ao repo
            
            for t in tags:
                if t.id in boxes:
                    bd_rep.tags.add(t)
                else:
                    bd_rep.tags.remove(t)
                bd_rep.save()

        elif "form2" in request.POST:
            tag_name = request.POST['tag_name']
            color = request.POST['color']
            create_tag(tag_name, color, creator)

        return HttpResponseRedirect('/app/repo/' + str(github_id))

def get_repos(username):

    api_url = '{}users/{}/repos?clientid={}&client_secret={}'.format(api_url_base, username,api_token, api_secret)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def create_tag(tag_name, color, user):
    new_tag = Tag(tag_name=tag_name, color=color, creator=user)
    new_tag.save()

def get_repotags(github_id):
    repo = Repository.objects.get(github_id=github_id)
    tags = repo.tags.all()
    return tags
    