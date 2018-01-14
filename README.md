# flaskr-app

### Application

Flask constructor takes the name of current module (__name__) as argument.

```
app.route(rule, options)
```
The rule parameter represents URL binding with the function.

The options is a list of parameters to be forwarded to the underlying Rule object.

Finally the run() method of Flask class runs the application on the local development server.
```
app.run(host, port, debug, options)
```

+--------------------------------------------------------------------------------------------
  host 																						|
  																							|
  Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally.																	  |
+--------------------------------------------------------------------------------------------

+-------------------+
  port				|
  					|
  Defaults to 5000  |
+-------------------+

+----------------------------------------------------------------+
debug															 |
																 |
Defaults to false. If set to true, provides a debug information  |
+----------------------------------------------------------------+

+----------------------------------------------+
options										   |
											   |
To be forwarded to underlying Werkzeug server. |
+----------------------------------------------+


### DEBUG MODE
The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.

+----------------------+
  DEBUG MODE 		   |
					   |
  app.debug = True 	   |
  app.run()			   |
  app.run(debug = True)|
+----------------------+

### VARIABLE RULES

In addition to the default string variable part, rules can be constructed using the following converters −

int
accepts integer

float
For floating point value

path
accepts slashes used as directory separator character

### FLASK URL BUILDING


The url_for() function is very useful for dynamically building a URL for a specific function. The function accepts the name of a function as first argument, and one or more keyword arguments, each corresponding to the variable part of URL.

url_for() is used for namespacing functions in django, can also pass in the arguments.

### HTTP METHODS

GET
Sends data in unencrypted form to the server. Most common method.

HEAD
Same as GET, but without response body

POST
Used to send HTML form data to server. Data received by POST method is not cached by server.

PUT
Replaces all current representations of the target resource with the uploaded content.

	
DELETE
Removes all current representations of the target resource given by a URL


### TEMPLATES

FLASK will search for a folder named templates.
Flask is based on Jinga2 templating system. (same like django)


The Jinga2 template engine uses the following delimiters for escaping from HTML.

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements

function used to render templates is `render_template`

### REQUEST OBJECTS


The data from a client’s web page is sent to the server as a global request object. In order to process the request data, it should be imported from the Flask module.

Important attributes of request object are listed below −

Form − It is a dictionary object containing key and value pairs of form parameters and their values.

args − parsed contents of query string which is part of URL after question mark (?).

Cookies − dictionary object holding Cookie names and values.

files − data pertaining to uploaded file.

method − current request method.

### COOKIES

A cookie is stored on a client’s computer in the form of a text file. Its purpose is to remember and track data pertaining to a client’s usage for better visitor experience and site statistics.

A Request object contains a cookie’s attribute. It is a dictionary object of all the cookie variables and their corresponding values, a client has transmitted. In addition to it, a cookie also stores its expiry time, path and domain name of the site.

In Flask, cookies are set on response object. Use make_response() function to get response object from return value of a view function. After that, use the set_cookie() function of response object to store a cookie.


