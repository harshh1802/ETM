from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User,auth
from .models import UserData

import sheet


def index(requests):

    if requests.method == 'POST':
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        userdata = UserData.objects.all()

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(requests, user)
            data = sheet.get_profile(requests.user.username)
            return render(requests, 'profile.html',{'userdata':data})
        else:
            return HttpResponseNotFound('Credentials not in database')

    else:
        return render(requests, 'index.html')


def profile(requests):
    data = sheet.get_profile(requests.user.username)
    print(data)
    return render(requests, 'profile.html',{'userdata':data})


def task(requests):

        data = sheet.get_task(requests.user.username)
        # params = {'tittle':data['tittle'], 'project': data['project'],'details':data['details'], 'allocation':data['allocation'],'deadline':data['deadline'],'docs':data['docs']}
        return render(requests, 'task.html',{'userdata':data})




def team(requests):
    userdata = UserData.objects.all()
    data = sheet.get_team()

    return render(requests, 'team.html', {'userdata': data})


def meet (requests):

    data = sheet.get_meet()
    return render(requests, 'meet.html',{'userdata':data})


def filter(requests):

    if requests.method == 'POST':
        pass

    else:
        pass


    return render(requests,'filter.html',params)






