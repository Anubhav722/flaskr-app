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

