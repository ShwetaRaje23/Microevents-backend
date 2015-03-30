from ..models import meManager


def manageRequest(request, event_id=None):
    # 2 cases, either accept or reject a event
    # also returns all events for you
    if request.method == "POST":
        if event_id is None:
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
        return getEvent(request, event_id)

    


def acceptEvent(request):
    event = request.POST.get('event_id','')
    user = request.POST.get('user_id','')
    circle = request.POST.get('circle_id','')
    
    row=meManager.objects.filter(event_id=event,user_id=user,circle_id=circle)
    row.accept = True
    row.save()
    
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")


def getEvents(request):
    user = request.POST.get('user_id','')
    
    all_events_for_user = meManger.objects.filter(user_id=user,accept=True)
    response=[]
    for event in all_events_for_user:
        eid = event.getResponseData()['event_id']
        
        event_row=meEvent.objects.filter(id=eid)
        response.append(event_row.getResponseData)
   return HttpResponse(json.dumps(response_data), content_type="application/json")     
