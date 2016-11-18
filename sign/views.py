from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sign.models import Event

# Create your views here.


def index(request):
    return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)  # 登录
        # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
        request.session['user'] = username
        response = HttpResponseRedirect('/event_manage/')
        return response
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username,"events":event_list})

