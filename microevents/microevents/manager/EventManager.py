from ..models import meEvents

def eventRequest(request, event_id=None):
        if (event_id is None):
            event_id = request.GET.get('event_id', '')
            
        if request.method == "POST":
            return createEvent(request)
        elif request.method == "DELETE":
            return deleteEvent(request,event_id)
        else:
            return getEvent(request,event_id)

def createEvent(request):
    eventName = request.POST.get('event_name','')
    eventDateTime = request.POST.get('event_date_time','')
    eventOwner = request.POST.get('user_id','')
    eventVenue = request.POST.get('venue','')
    
    event = meEvent()
    event.name = eventName
    event.date_time = eventDateTime
    event.owner = eventOwner
    event.venue = eventVenue

    event.save()
    response_data = chore.getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def deleteEvent(request,event_id):
    event = meEvent.objects.get(id=event_id)
    event.delete()
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")

def getEvent(request,event_id):
    response_data = {}

    if event_id:
        meEvent = meEvents.objects.filter(id=event_id)

        #Ideally there shouldn't be duplicate users.
        if len(meEvent)>0:
            event = tievent[0]
            response_data = event.getResponseData()

    return HttpResponse(json.dumps(response_data), content_type="application/json")

