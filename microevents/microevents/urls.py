from django.conf.urls import patterns, include, url
#from django.contrib import admin
from manager import UserManager
from manager import LoginManager
from manager import EventManager
from manager import CircleManager

urlpatterns = patterns('',
                       url(r'^api/login/$', LoginManager.loginRequest),
                       url(r'^api/logout/$', LoginManager.logUserOut),
                       url(r'^api/testlogin/$', LoginManager.getCurrentUserJson),
                       url(r'^api/csrf/$', LoginManager.tokenRequest),

                       url(r'^api/user/$', UserManager.userRequest),
                       url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest),
                       url(r'^api/user/((?P<user_id>\d+)/)?edit/$', UserManager.editUserRequest),


                       url(r'^api/event/$', EventManager.eventRequest),
                       url(r'^api/event/(?P<event_id>\d*)/$', EventManager.eventRequest),

                       url(r'^api/circle/$', CircleManager.circleRequest),
                       url(r'^api/circle/(?P<circle_id>\d*)/$', CircleManager.circleRequest)
)

