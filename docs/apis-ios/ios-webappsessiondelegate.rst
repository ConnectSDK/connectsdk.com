WebAppSessionDelegate
=====================

WebAppSessionDelegate provides callback methods for receiving messages
from a running web app.

Methods
-------

\- (void) **webAppSession**:(`WebAppSession </apis/1-6-0/ios/WebAppSession>`__ \*)\ *webAppSession* **didReceiveMessage**:(id)\ *message*
   This method is called when a message is received from a web app.

   **Parameters:**

   -  webAppSession – WebAppSession that corresponds to the web app that sent the
      message

   -  **didReceiveMessage**: message – Message from the web app, either an NSString or a JSON object in
      the form of an NSDictionary

\- (void) **webAppSessionDidDisconnect**:(`WebAppSession </apis/1-6-0/ios/WebAppSession>`__ \*)\ *webAppSession*
   This method is called when a web app's communication channel
   (WebSocket, etc) has become disconnected.

   **Parameters:**

   -  webAppSession – WebAppSession that became disconnected
