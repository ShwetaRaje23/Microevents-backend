from ..models import meCircles

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
    owner =  request.POST.get('user_id', '')

    for user_id in user_ids:
        circle =  meCircle()
        circle.circle_name = circleName
        circle.group_users = user_id
        circle.save()

def getCircle(request,circle_id):
    response_data = {}

    if circle_id:
        meCircle = meCircles.objects.filter(id=circle_id)
        #Ideally there shouldn't be duplicate users.
        if len(meCircle)>0:
            circle = meCircle[0]
            print "feaegearewr"
            
            response_data = group.getResponseData(request)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

        
def deleteCircle(request, circle_id):
    response_data = {"success":False}
    if circle_id:
        mecircles = meCircle.objects.filter(id=circle_id)
        #Ideally there shouldn't be duplicate circles
        if len(ticircles)>0:
            circle = mecircles[0]
            # if circle.circleUsers.count()>1:
            #     #1 because "this" user is attempting to delete it
            #     response_data["reason"] = "This circle has other users. You cannot delete it"
            # else:
            #     print "Got Circle. Now deleting it"

            circle.delete()
            response_data["success"] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")

    
