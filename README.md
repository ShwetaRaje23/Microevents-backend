Microevents-Backend
===================

Backend for microevents
MICROEVENTS 

REST API Documentation 

    Please note that all urls should have a trailing slash ( / ). Some requests will work without it, but others won't. 

Logging In/Out 
======

Login    
```
    POST /api/login/ 
    Sample request: 
    { 
        email: "rahul@goel.com" 
    } 
```
Logout
```
    POST /api/logout/  
    
    No params required 
```

Users 
======

Get User
If user_id is omitted, it uses the user_id of the current user (if logged in) 
```
    GET /api/user/<user_id>/ 
    Sample response: 
    { 
        users{
        first_name: "Rahul", 
        last_name: "Goel", 
        email: "rahul@goel.com", 
        user_id: 1,
        },
        events{}
        
    } 
```
Create User
If a user with that email address already exists, { success: false } is returned. 
```
    POST /api/user/ 
    Sample request: 
    { 
        first_name: "John", 
        last_name: "Smith", 
        email: "johnsmith@gmail.com" 
    } 
```
Edit the properties of a user. user_id is optional. Only first_name, last_name, email are editable. 
```    
    POST /api/user/<user_id>/edit/ 
    Sample request: 
{ 
    first_name: 'John', 
    email: 'johnsmith@gmail.com' 
    //here, last_name will remain the same 
} 

```
Get all events for user
```
   POST /api/main/
 
{
    user_id="2"
}
```

Events 
======
Returns the event with <event_id>. 
```
    GET /api/event/<event_id>/  
    Sample response: 
{ 
    event_id: 1, 
    venue: "Atlanta", 
    date_time:”2012-11-23 11:11:00” 
    owner_id:1 
    event_name:”event1” 
} 

```
Creates an event and returns it and automatically creates a manager object that maps event, circle_id, user_id and invite acceptance. 
```
    POST /api/event/  
    Sample request:
{ 
    event_name: "sample event" 
    event_date_time:”2012-11-23 11:11:00” 
    user_id:1 
    venue: “Atlanta” 
    invites: cricleid1,circleid2.. 
} 
```
Creates an event and returns it. 
```
    POST /api/ event/<event_id>/ 
    Sample request: 
{ 
    event_name: "sample event" 
    event_date_time:”2012-11-23 11:11:00” 
    user_id:1 
    venue: “Atlanta” 
    invites: cricleid1,circleid2.. 
} 
```
Deletes an event if event exists 
```
    DELETE /api/ event/<event_id>/ 
```
Circles
======
Returns the circle with the circle id. 
```
    GET /api/circle/<circle_id>/ 
    Sample response: 
{ 
    circle_name: myCircle, 
    users: /*not sure what data this returns*/, 
    owner: false 
} 
```
Creates a circle. 
```
    POST /api/circle/ 
    Sample request: 
{ 
    circle_name: 'myCircle', 
    user_ids: user_id1,user_id2 ....., 
    user_id: user_id (owner_id) 
} 
```
Deletes a circle item. 
```
    DELETE /api/ circle/<circle_id>/ 
```
 Get all circels for user
 
```
    GET /api/ circle/?user_id=1 
```
