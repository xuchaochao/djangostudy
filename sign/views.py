from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


# def index(request):
#     return HttpResponse("hello django~")


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
        # if username == "admin" and password == "admin123":
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie("user", username, 3600)
            # return HttpResponse("login success~")
            request.session["user"] = username
            return response
        else:
            return render(request, "index.html", {"error":"username or password not right !"})


@login_required
def event_manage(request):
    # username = request.COOKIES.get("user", "")
    username = request.session.get("user", "")
    return render(request, "event_manage.html", {"user":username})

