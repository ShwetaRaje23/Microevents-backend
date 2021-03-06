import json
from django.http import HttpResponse
from ..models import meEvents,meUser,meCircles,meManager
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
@csrf_exempt
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
        owner_id = request.POST.get('user_id','')
        eventVenue = request.POST.get('venue','')
        invitedCircles = request.POST.get('invites','')
        invitedCircles = invitedCircles.split(',')
        event = meEvents()
        event.event_name = eventName
        dateobj = datetime.strptime(eventDateTime,'%Y-%m-%d %H:%M')

        event.date_time = dateobj
        eventOwner = meUser.objects.get(id=owner_id)
        event.owner = eventOwner
        event.venue = eventVenue
        event.save()
        eid = event.id
        
        if createManager(invitedCircles,eid)==False:
                response_data = event.getResponseData()
                # return HttpResponse(json.dumps(response_data), content_type="application/json")
                return HttpResponse(json.dumps({'success': False}), content_type="application/json")
        
        response_data = event.getResponseData()
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def createManager(invitedCircles,eid):
        print "reaching here",invitedCircles
        for circle_id in invitedCircles:
                print "reaching here wer ",circle_id
                try:
                        print "tsete"
                        circle = meCircles.objects.filter(id=circle_id)
                except:
                        return False
                
                print circle

                if len(circle) is 0:
                        print "circle not existant"
                        return False
                circle = circle[0]
                print circle_id
                data_cir = circle.getResponseData()
                for user in data_cir["users"]:
                        manager = meManager()
                        event = meEvents.objects.filter(id=eid)
                        if(len(event) is 0):
                                print "event not existant,shouldnt happen"
                                return False
                        manager.event = event[0]
                        manager.user_id = user['user_id'] # should be a user
                        print "Creating row for ",user['user_id'],event[0].id
                        manager.accept = 0
                        manager.circle_id = circle_id
                        manager.save()
        return True


def deleteEvent(request,event_id):
        event = meEvents.objects.get(id=event_id)
        event[0].delete()
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

@csrf_exempt
def getEventOfOwner(request,user_id):
    response_data=[]
    
    # user_id = request.GET.get('user_id','')
    
    if user_id:
        meEventOwner = meEvents.objects.filter(owner=user_id)

    if len(meEventOwner)>0:
        for eachEvent in meEventOwner:
            event = eachEvent.getResponseData()
            response_data.append(event)

    else:
        return HttpResponse(json.dumps({'success':False}), content_type="application/json")


    return HttpResponse(json.dumps(response_data), content_type="application/json")
                
