from django.db import models
from datetime import datetime, timedelta


class meUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def getResponseData(self):

        #Create Resposne Dictionary
        response_data = {}
        response_data["first_name"] = self.first_name
        response_data["last_name"] = self.last_name
        response_data["email"] = self.email
        response_data["user_id"] = self.id

        return response_data

class meCircles(models.Model):
    circle_id = models.IntegerField(default=0)
    circle_name = models.CharField(max_length=30)
    group_users = models.ManyToManyField('meUser')
    circle_owner = models.ForeignKey('meUser')
    
    def __unicode__(self):
        return self.circle_name
    
    def getResponseData(self, request=None):
        user_id = None
        if request:
            user_id = request.session['user_id']

        
        users=[]
        for i,user in enumerate(self.group_users.all()):
            if user.id == user_id and i !=0:
                temp = users[0]
                users[0] = user.getResponseData()
                users.append(temp)
        
        response_data={}
        response_data["circle_name"]=self.circle_name
        response_data["users"]=users
        
class meMananger(models.Model):
    event_id = models.IntegerField(default=0)
    circle_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    accept = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u"EventID:%d circleID:%d" %(self.event_id,self.circle_id)

    
class meEvents(models.Model):
    event_id = models.IntegerField(default=0)
    venue = models.CharField(max_length=30)
    date_time = models.DateTimeField(blank=True,null = True)
    owner = models.ForeignKey('meUser')
    