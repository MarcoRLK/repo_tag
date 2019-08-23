from django.shortcuts import render

# Create your views here.

def login_page(request):
	return render(request, 'login.html')

def logout_page(request):
	return render(request, 'login.html')