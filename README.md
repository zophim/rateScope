Build an application with django backend 
with 3 routes /, /login, /logout
/ page displays "anonymous" if nobody is logged in
/ page displays the username if a user is logged in
/login displays the standard user name and password and and redirects the user to / on successful login 
SEO on / content is important
/ is very db read heavy and hence should be CACHED
jinja/jade/jinja.jade templates would be nice to have, but not a hard requirement
Don't worry about /signup .... just seed the db 
Don't worry about css


Assumptions: (for design considerations only ... please do not implement any of the specifics mentioned below) 
/ contains a large number of rateable objects (pics, articles etc) whose display state changes as follows
if the user is anonymous, display "login to rate"
if the logged in user has rated the object, display user ratings
if the logged in user has not rated that object, display (invitation to rate)
Please do NOT have to implement the objects or its contents or rating 
20% traffic is anonymous users and the other 80% spread across a very LARGE number of logged in users
Please implement two caching solutions (preferably on two branches) 

Please feel free to reach out if you need any clarifications.
