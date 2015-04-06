import json
from django.http import HttpResponse
from ..models import meUser,meEvents,meCircles,meManager
from django.views.decorators.csrf import csrf_exempt
from LoginManager import getCurrentUser
from datetime import datetime, timedelta


@csrf_exempt
def userRequest(request, user_id=None):
    if (user_id is None):
        user_id = request.GET.get('user_id')
        user = getCurrentUser(request)
        if user:
            user_id = user.id
        #else error

    if request.method == "POST":
        return createUser(request)
    else:
        return getUser(request, user_id)

@csrf_exempt
def editUserRequest(request, user_id=None):
    if user_id is None:
        curr_user = getCurrentUser(request)
        if curr_user:
            user_id = curr_user.id

    if user_id:
        user = meUser.objects.get(id=user_id)

        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email

        user.save()
        return HttpResponse(json.dumps({'success': True}), content_type="application/json")
    return HttpResponse(json.dumps({'success': False}), content_type="application/json")

@csrf_exempt
def createUser(request):
    first_name = request.POST.get('first_name','')
    last_name = request.POST.get('last_name','')
    email = request.POST.get('email','')
    user = None
    existing_users = meUser.objects.filter(email=email)

    if len(existing_users) > 0:
        existing_user = existing_users[0]
        if existing_user.first_name == "Unverified" and existing_user.last_name == "Unverified": #hardcoded new user
            user = existing_user
        else:
            # we already have a user with that email.
            return HttpResponse(json.dumps({'success': False}), content_type="application/json")

    if user is None:
        user = meUser()
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()
    response_data = user.getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getUser(request, user_id):
    response_data = {}
    # print "tesrt",user_id
    if user_id:
        meusers = meUser.objects.filter(id=user_id)
        #Ideally there shouldn't be duplicate users.
        # print "gesr"
        if len(meusers)>0:
            user = meusers[0]
            events_with_user_is_owner=meEvents.objects.filter(owner=user)
            events_dict={}
            for events in events_with_user_is_owner:
                res=events.getResponseData()
                events_dict.append(res)
            response_data['user'] = user.getResponseData()
            response_data['events'] = events_dict

    return HttpResponse(json.dumps(response_data), content_type="application/json")


