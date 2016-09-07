<h1 style="text-align: center; margin-bottom: -20px;">Office Sign Up</h1>
##Description
Sign up system for office. Based on Python micro web framework [Flask 0.10.1](http://flask.pocoo.org/) and connected with MySQL database by python [official MySQL connector](http://dev.mysql.com/doc/connector-python/en/).

##Installation
* Execute ```db/tables.sql``` on MySQL command line or phpMyAdmin to create all necesaries tables.
* Edit ```model/__init__.py``` to set your database access info.
* **IMPORTANT** If you going to call api externally you must specificy the *wild card* IP address on line 125:
	````
   app.run(<int:ip address>)
    ````
* If you wont specific port to run on your server, edit ```__main__.py``` and set your custom port on line 125:
	```
app.run(port=<int:port>)
    ```
* Execute ```python __main__.py```

##Index
1. **Auth**
	1.1 Check token
	1.2 Login
	1.3 Logout
2. **Session**
	2.1 Get sessions
	2.2 Get session by ID
	2.3 Get session by employee ID
	2.4 Get session hours by employee ID
	2.5 Create session
	2.6 Update existing session
	2.7 Delete session
3. **Employee**
	3.1 Get employees
	3.2 Get employee by ID
	3.3 Create employee
	3.4 Update existing employee
	3.5 Delete employee

##Content
###1. AUTH
Send to admin user generated token to execute actions with employees and sessions.
####1.1 Check token
---
Check if token is valid or expired.
#####Request <span class="protocol green">GET</span> ```/auth/```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 403</span>
**Body** [type: plain text]
```
	Forbidden
```
___
####1.2 Login
---
Request access token from HTTP Basic Auth protocol.
#####Request <span class="protocol blue">POST</span> ```/auth/```
**Headers**
```
	Authorization: <string:base64_encode(username:password)>
```
#####Response <span class="status green">OK 200</span>
**Body**
```
	{
    	username: <string:username>, 
        token: <string:token_generated>, 
        email: <string:email address>, 
        expire: <datetime:token_expire_date>
     }
```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####1.3 Logout
---
Logout and set token to empty string and expire to zero datetime.
#####Request <span class="protocol red">DELETE</span> ```/auth/```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
###SESSION
Module to display and control employees session info. 
####2.1 Get sessions
---
Show all sessions on database.
#####Request <span class="protocol green">GET</span> ```/session/```
**Headers**
```
	token: <string:user_token>
```
**URL Parameters** [Optional]
```
	from=<date:sessions day>
    to=<date:sessions day>
```

#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
	[
    	{
        	id: <int:session id>,
            day: <date:session day>,
        	start: <time: session start>, 
            end: <time: session end>,  
            employee: {
            	id: <int:employee id>,
                name: <string:full name>, 
                email: <string:email address>,  
                fingerprint: <string:employee hex fingerprint>
            }
        },
		...
     ]

```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.2 Get session by ID
---
Show sessions filtered by session id.
#####Request <span class="protocol green">GET</span> ```/session/<int:session id>```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
    {
        id: <int:session id>,
        day: <date:session day>,
        start: <time: session start>, 
        end: <time: session end>, 
        employee: {
            id: <int:employee id>,
            name: <string:full name>, 
            email: <string:email address>, 
            fingerprint: <string:employee hex fingerprint>
        }
    }
```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.3 Get session by employee ID
---
Show sessions filtered by session id.
#####Request <span class="protocol green">GET</span> ```/session/employee/<int:session id>```
**Headers**
```
	token: <string:user_token>
```
**URL Parameters** [Optional]
```
	from=<date:sessions day>
```
or
```
	from=<date:sessions day>
    to=<date:sessions day>
```
#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
	[       
       {
            id: <int:session id>,
            day: <date:session day>,
            start: <time: session start>, 
            end: <time: session end>, 
            employee: {
                id: <int:employee id>,
                name: <string:full name>, 
                email: <string:email address>, 
                fingerprint: <string:employee hex fingerprint>
            }
        },
        ...
     ]
```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.4 Get session hours by employee ID
---
Show sessions filtered by session id.
#####Request <span class="protocol green">GET</span> ```/session/employee/<int:session id>/hours```
**Headers**
```
	token: <string:user_token>
```
**URL Parameters** [Optional]
```
	from=<date:sessions day>
```
or
```
	from=<date:sessions day>
    to=<date:sessions day>
```
#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
    {
        to: <date:sessions daterange starts>,
        from: <date:sessions daterange ends>,
        hours: <int:session hours on daterange>,
        minutes: <int:session minutes on daterange>,
    	employee_id: <int:employee id>
    }
```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.5 Create session
---
Creates new session.
#####Request <span class="protocol blue">POST</span> ```/session/```
**Headers**
```
	token: <string:user_token>
```
**Body**
```
	day: <date:session day>
    start: <time: session start>
    end: <time: session end> [Optional]
    employee: <int:employee id>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.6 Update session
---
Update session based on its id.
#####Request <span class="protocol orange">PUT</span> ```/session/<int:session id>```
**Headers**
```
	token: <string:user_token>
```
**Body**
```
	day: <date:session day>
    start: <time: session start>
    end: <time: session end>
    employee: <int:employee id>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####2.7 Delete session
---
Delete session from database.
#####Request <span class="protocol red">DELETE</span> ```/session/<int:session id>```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
###EMPLOYEE
Module to display and control employees info. 
####3.1 Get employees
---
Return list with all employees.
#####Request <span class="protocol green">GET</span> ```/employee/```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
	[
    	{
        	id: <int:user id>,
        	name: <string:full name>, 
            email: <string:email adress>,  
            fingerprint: <string:employee hex fingerprint>
        },
		...
     ]

```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####3.2 Get employee by ID
---
Return employee info based on id.
#####Request <span class="protocol green">GET</span> ```/employee/<int:employee id>```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
**Body** [type: json]
```
    {
        id: <int:user id>,
        name: <string:full name>,
        email: <string:email adress>,
        fingerprint: <string:employee hex fingerprint>
    }
```
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####3.3 Create employee
---
Create new employee.
#####Request <span class="protocol blue">POST</span> ```/employee/```
**Headers** 
```
	token: <string:user_token>
```
**Body**
```
	name: <string:full name>,
    email: <string:email adress>,
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####3.4 Update employee
---
Update employee based on id.
#####Request <span class="protocol orange">PUT</span> ```/employee/<int:employee id>```
**Headers**
```
	token: <string:user_token>
```
**Body**
```
	name: <string:full name>,
    email: <string:email adress>,
    fingerprint: <string:finguerprint_signature>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
___
####3.5 Delete employee
---
Delete employee.
#####Request <span class="protocol red">DELETE</span> ```/employee/<int:employee id>```
**Headers**
```
	token: <string:user_token>
```
#####Response <span class="status green">OK 200</span>
#####Response <span class="status red">ERROR 4XX</span>
**Body** [type: plain text]
```
	<string:error message>
```
#####Response <span class="status blue">ERROR 5XX</span>
**Body** [type: plain text]
```
	<string:error message>
```