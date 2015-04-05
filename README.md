Microevents-Backend
===================

Backend for microevents
MICROEVENTS 

REST API Documentation 

    Please note that all urls should have a trailing slash ( / ). Some requests will work without it, but others won't. 

Logging In/Out 
    Logs the user into the app with email. 
    POST /api/login/ 
    Sample request: 
    { 
        email: "rahul@goel.com" 
    } 

    POST /api/logout/  

    Logs out the current user. 

    No params required 

Users 

    GET /api/user/<user_id>/ 

    Returns the user with <user_id>.  

    If user_id is omitted, it uses the user_id of the current user (if logged in) 

    Sample response: 

{ 

   first_name: "Rahul", 

     last_name: "Goel", 

   email: "rahul@goel.com", 

     user_id: 1, 

} 

    POST /api/user/ 

    Creates a user and returns it. 

    If a user with that email address already exists, { success: false } is returned. 

    Sample request: 

{ 

    first_name: "John", 

    last_name: "Smith", 

    email: "johnsmith@gmail.com" 

} 

    POST /api/user/<user_id>/edit/ 

    Edit the properties of a user. 

    user_id is optional. 

    Only first_name, last_name, email are editable. 

    Sample request: 

{ 

    first_name: 'John', 

    email: 'johnsmith@gmail.com' 

    //here, last_name will remain the same 

} 

 

Events 

    GET /api/event/<event_id>/  

    Returns the event with <event_id>. 

    Sample response: 

{ 

    event_id: 1, 

    venue: "Atlanta", 

  date_time:”2012-11-23 11:11:00” 

  owner_id:1 

  event_name:”event1” 

} 

    POST /api/event/  

    Creates an event and returns it and automatically creates a manager object that maps event, circle_id, user_id and invite acceptance. 

    Sample request: 

{ 

    event_name: "sample event" 

  event_date_time:”2012-11-23 11:11:00” 

  user_id:1 

  venue: “Atlanta” 

  invites: cricleid1,circleid2.. 

} 

    POST /api/ event/<event_id>/ 

    Creates an event and returns it. 

    Sample request: 

{ 

    event_name: "sample event" 

  event_date_time:”2012-11-23 11:11:00” 

  user_id:1 

  venue: “Atlanta” 

  invites: cricleid1,circleid2.. 

} 

    DELETE /api/ event/<event_id>/ 

    Deletes an event if event exists 

Circles 

    GET /api/circle/<circle_id>/ 

    Returns the circle with the circle id. 

    Sample response: 

{ 

    circle_name: myCircle, 

    users: /*not sure what data this returns*/, 

    owner: false 

} 

    POST /api/circle/ 

    Creates a circle. 

    Sample request: 

{ 

    circle_name: 'myCircle', 

    user_ids: user_id1,user_id2 ....., 

    user_id: user_id (owner_id) 

} 

    DELETE /api/ circle/<circle_id>/ 

    Deletes a circle item. 

 

 
Get all events for user

    
        POST /api/main/
 
{
    user_id="2"
}
 

 
