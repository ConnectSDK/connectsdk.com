WebAppSessionListener 
===========================================================================
``com.connectsdk.service.sessions.WebAppSessionListener``

Methods
-------

void **onReceiveMessage** (:doc:`WebAppSession <and-webappsession>` *webAppSession*, Object *message*)
   
    This method is called when a message is received from a web app.

    **Parameters:**
        * webAppSession – WebAppSession that corresponds to the web app that sent the message
        * message – Object from the web app, either an String or a JSONObject

void **onWebAppSessionDisconnect** (:doc:`WebAppSession <and-webappsession>` *webAppSession*)
   
    This method is called when a web app's communication channel
    (WebSocket, etc) has become disconnected.

    **Parameters:**
        * webAppSession – WebAppSession that became disconnected
