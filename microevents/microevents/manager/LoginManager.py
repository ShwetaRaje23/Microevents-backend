import json
import random
import string
from django.http import HttpResponse
from ..models import meUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getCurrentUserJson(request):
    user = getCurrentUser(request)
    response_data = {}
    if user:
        response_data = user.getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getCurrentUser(request):
    ####HARDCODED just for demo/dev purposes###
    user = meUser.objects.filter(email='brandonchastain@gmail.com')

    #Whenever getting something from the database, check that only one
    #object was returned. Multiple users with the same email (unlikely but not impossible)
    #will cause the app to crash with the error "MultipleObjectsReturned: get() returned more than one .."
    if len(user)>0:
            user = user[0]

    return user
    ####

   # if ('current_user_id' in request.session):
   #    user_id = request.session['current_user_id']
   #     users = TIUser.objects.filter(id=user_id)
   #     if len(users)>0:
   #         return users[0]
   # return None

@csrf_exempt
def loginRequest(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        return logUserIn(request, email)

def logUserIn(request, email):
    ####HARDCODED just for demo/dev purposes###
    #return HttpResponse(json.dumps({'success': True}), content_type="application/json")
    ####
    users = meUser.objects.filter(email=email)
    if len(users)>0:
        user = users[0]
        #request.session['current_user_id'] = user.id
        return HttpResponse(json.dumps(user.getResponseData()), content_type="application/json")
    return HttpResponse(json.dumps({'success': False}), content_type="application/json")

@csrf_exempt
def logUserOut(request):
    ####HARDCODED don't log out if in dev
    #request.session['current_user_id'] = None
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")


@csrf_exempt
def tokenRequest(request):
    if request.method == "GET":
        return generateCSRFToken(request)

def generateCSRFToken(request):
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                  for x in xrange(32))
    request.session['state'] = state
    response = {
        'CLIENT_ID': '1014642982140-m7f0706v4g3cl01d476ik331nj6gntq1.apps.googleusercontent.com',
        'state': state,
        'APPLICATION_NAME': 'MicroEvents'
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
