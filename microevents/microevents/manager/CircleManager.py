import json
from django.http import HttpResponse
from ..models import meEvents,meUser,meCircles
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def circleRequest(request,circle_id=None):
    if (circle_id is None):
        circle_id = request.GET.get('circle_id', '')
    if request.method == "POST":
        return createCircle(request)
    elif request.method == "DELETE":
        return deleteCircle(request, circle_id)
    else:
        return getCircle(request, circle_id)

def createCircle(request):
    circleName = request.POST.get('circle_name', '')
    user_ids = request.POST.get('user_ids', '')
    owner_id =  request.POST.get('user_id', '')
    user_ids= user_ids.split(',')
    circle =  meCircles()
    circle.circle_name = circleName
    circle.circle_owner=meUser.objects.filter(id=owner_id)[0]

    users=[]
    for user_id in user_ids:    
        print user_id
        current_user = meUser.objects.filter(id=user_id)
        # print current_user
        if current_user is None or len(current_user)==0:
            return HttpResponse(json.dumps({'success': False}), content_type="application/json")
        users.append(current_user[0])
    circle.save()
    print users
    circle.group_users = users
    circle.save()
    response_data = circle.getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getCircle(request,circle_id):
    response_data = {}

    if circle_id:
        meCircle = meCircles.objects.filter(id=circle_id)
        #Ideally there shouldn't be duplicate users.
        if len(meCircle)>0:
            circle = meCircle[0]
            print "feaegearewr"
            
            response_data = meCircle.getResponseData(request)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

        
def deleteCircle(request, circle_id):
    response_data = {"success":False}
    if circle_id:
        mecircle = meCircles.objects.filter(id=circle_id)
        #Ideally there shouldn't be duplicate circles
        if len(mecircle)>0:
            circle = mecircle[0]
            # if circle.circleUsers.count()>1:
            #     #1 because "this" user is attempting to delete it
            #     response_data["reason"] = "This circle has other users. You cannot delete it"
            # else:
            #     print "Got Circle. Now deleting it"

            circle.delete()
            response_data["success"] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")

    
