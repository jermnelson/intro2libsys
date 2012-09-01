"""
 :mod:`views` Learner views for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext

def logout_view(request):
    """
    Logs out Learner and redirects to DSL home

    :param request: HTTP request
    """
    logout(request)
    redirect("home")

def login_view(request):
    """
    Display's a login for a user.

    :param request: HTTP request
    """
    if request.method == 'GET':
        login_form = AuthenticationForm()
        return render_to_response('learner-login.html',
                                  {"login_form":login_form},
                                   context_instance=RequestContext(request))
    username = request.POST['username']
    password = request.POST['password']
    if request.POST.has_key("redirect-url"):
        redirect_url = request.POST["redirect-url"]
    else:
        redirect_url = "Learner-profile"
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            redirect(redirect_url)
        else:
            return render_to_response('learner-error.html',
                                      {"message":'disabled account'},
                                       mimetype="application/xhtml+xml")

           
    else:
       return render_to_response('learner-error.html',
                                 {"message":'invalid login'},
                                   mimetype="application/xhtml+xml")


@login_required
def profile(request):
    """
    Displays a Learner's profile
   
    :param request: HTTP request
    """
    return render_to_response("profile.html",
                              {"assessments":[],
                               "attendance":[],
                               "learner":None},
                              mimetype="application/xhtml+xml")


@login_required
def update(request):
    """
    Update a Learner's profile

    :param request: HTTP request
    """
    return None

