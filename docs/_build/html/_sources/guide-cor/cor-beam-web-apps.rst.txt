Beam Web Apps
=============

There are several platforms available which support the launching of web
apps. A web app is typically run on a temporary basis in a full-screen
browser instance.

Web App IDs
-----------

Both webOS and Chromecast platforms require a web app ID for API calls
to launch & communicate with web apps. This web app ID is translated it
into your web app's URL on web app launch.

For information on creating a web app ID for webOS, please visit the
`registration site`_.

To learn how to register for a Chromecast web app ID, visit \`Google's
app ID registration site`_\ .


.. _registration site: http://lgsvl.com/connectSDK/index.php
.. _Google's app ID registration site: https://developers.google.com/cast/docs/registration

Launch web app with identifier
------------------------------

Connect SDK currently supports web app launching on webOS and Chromecast
devices, which both translate a web app identifier into your web app's
URL.

Communicate with web app
------------------------

Bi-directional communication with your web app is made extremely simple.
Data can be sent and received strongly-typed as a string or a keyed set
of values (JSON object).

.. code-block:: javascript

   var webAppId;

   if (device.hasService(ConnectSDK.Services.WebOSTV)) {
       webAppId = "5G7328DE";
   } else if (device.hasService(ConnectSDK.Services.Chromecast)) {
       webAppId = "3E5106AB";
   } else if (device.hasService(ConnectSDK.Services.AirPlay)) {
       webAppId = "http://www.example.com/";
   }

   if (!webAppId) {
       return;
   }

   device.getWebAppLauncher().launchWebApp(webAppId).success(function (session) {
       console.log("web app launch success");
   }).error(function (err) {
       console.log("web app launch error: " + err.message);
   });

.. code-block:: javascript

   var mySession = null;
   var webAppId;


   if (device.hasService(ConnectSDK.Services.WebOSTV)) {
       webAppId = "5G7328DE";
   } else if (device.hasService(ConnectSDK.Services.Chromecast)) {
       webAppId = "3E5106AB";
   }

   if (!webAppId) {
       return;
   }

   device.getWebAppLauncher().launchWebApp(webAppId).success(function (session) {
       // Keep a reference to the session
       mySession = session.acquire();

       // Open a communication channel to the app
       mySession.connect().success(function () {
           console.log("web app connect success");
       }).error(function (err) {
           console.log("web app connect error: " + err.message);
       });

       // Make sure to release the session when done using it
       mySession.on("disconnect", function () {
           mySession.release();
           mySession = null;
       });
   }).error(function (err) {
       console.log("web app launch error: " + err.message);
   });

After successfully establishing a connection, you can send messages to
your web app.

.. code-block:: javascript

   mySession.sendText("This is a test message");

You can also send a Javascript dictionary object which will be received
by the web app as an object.

.. code-block:: javascript

   var message = {
       someParameter: "someValue",
       anArray: ["array value 1", "array value 2", "array value 3"],
       anotherObject: {
           anotherParameter: "anotherValue"
       }
   };

   mySession.sendJSON(message);

The "message" event allows you to receive messages from your web app.

.. code-block:: javascript

   mySession.on("message", function (message) {
       console.log("Received message from web app:" + JSON.stringify(message));
   });
