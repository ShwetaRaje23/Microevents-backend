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
        invitedCircles = request.POST.get('invites','')
        event = meEvents()
        event.event_name = eventName
        event.date_time = eventDateTime
        event.owner = eventOwner
        event.venue = eventVenue
        event.save()
        eid = event.id
        createManager(invitedCircles,eid)
        response_data = event.getResponseData()
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def createManager(invitedCircles,eid):
        
        for circle_id in invitedCircles:
                circle = meCircles.objects.filter(id=circle_id)
                data_cir = circle.getResponseData()
                for user in data_cir["users"]:
                        manager = meManager()
                        manager.event_id = eid
                        manager.user_id = user # should be a user
                        manager.accpet = False
                        manager.circle_id = circle_id
                        manager.save()


def deleteEvent(request,event_id):
        event = meEvents.objects.get(id=event_id)
        event.delete()
        return HttpResponse(json.dumps({'success': True}), content_type="application/json")

def getEvent(request,event_id):
        response_data = {}

    if event_id:
            meEvent = meEvents.objects.filter(id=event_id)

        #Ideally there shouldn't be duplicate users.
        if len(meEvent)>0:
                event = meEvent[0]
                response_data = event.getResponseData()

    return HttpResponse(json.dumps(response_data), content_type="application/json")

