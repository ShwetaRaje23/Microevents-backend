from ..models import meManager
from ..models import meEvents
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def manageRequest(request, event_id=None):
    # 2 cases, either accept or reject a event
    # also returns all events for you
    if request.method == "GET":
        if event_id is None:
            return getEvents(request)
    if request.method == "POST":
        return acceptEvent(request)
        # else:
            # return editEvent(request,event_id)
    # elif request.method == "DELETE":
    #     if (event_id is None):
    #         event_id = request.DELETE.get('event_id', '')
    #     return deleteEvent(request, event_id)
    else:
        if (event_id is None):
            event_id = request.GET.get('event_id', '')
        return getEvents(request)

    


def acceptEvent(request):
    event = request.POST.get('event_id','')
    user = request.POST.get('user_id','')
    # circle = request.POST.get('circle_id','') #lets see for the circle id part
    accept = request.POST.get('accept')
    row=meManager.objects.filter(event_id=event,user_id=user)
    try:
        row=row[0]
    except:
        return HttpResponse(json.dumps({'success': False}), content_type="application/json")
    if(accept==1):
        row.accept = 1
    else:
        row.accept = 2
    row.save()
    
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")


def getEvents(request):
    print "fesse"
    user = request.GET.get('user_id','')
    print user
    all_events_for_user = meManager.objects.filter(user_id=user)
    print all_events_for_user
    response=[]
    for manage in all_events_for_user:
        # eid = event.getResponseData()['event_id']
        event = manage.event
        eid = event.id
        status = manage.accept
        print eid
        event_row = meEvents.objects.filter(id=eid)
        event_row = event_row[0]
        print "jere",event_row
        res = event_row.getResponseData()
        res['status'] = status
        response.append(res)
        
    return HttpResponse(json.dumps(response), content_type="application/json")
