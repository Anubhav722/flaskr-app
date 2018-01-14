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