Create a TV Web App
===================

Connecting a web app with the JavaScript bridge is incredibly simple and
requires a minimum amount of effort. First, make sure you've got the
right scripts imported.

-  Google Cast SDK `JavaScript Receiver
   file <https://developers.google.com/cast/docs/downloads>`__
-  Connect SDK `JavaScript
   Bridge <https://github.com/ConnectSDK/Connect-SDK-JavaScript-Bridge>`__

.. code-block:: html

   <script src="//www.gstatic.com/cast/sdk/libs/receiver/2.0.0/cast_receiver.js" language="JavaScript" type="text/javascript"></script>
   <script src="connect_bridge.min.js" language="JavaScript" type="text/javascript"></script>

After scripts are imported, it is a simple matter to get your app
configured. No matter what platform you are running on, the proper setup
will occur to enable your web app.

.. code-block:: javascript

   window.connectManager = new connectsdk.ConnectManager();
   window.connectManager.init();

Of course, if you actually want to enable any functionality in your web
app, you will have to do a little more work. Integration with Connect
SDK happens on two different levels.

Media playback and control
--------------------------

.. code-block:: javascript

   window.mediaElement = document.getElementById('media');
   window.connectManager.setMediaElement(window.mediaElement);

Bi-directional communication
----------------------------

Receiving messages
~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   window.connectManager.on("message", function(data) {
       console.log("Got message from sender " + data.from);
       console.log("Got message from mobile device " + data.message);
   });

Sending messages
~~~~~~~~~~~~~~~~

.. code-block:: javascript

   window.connectManager.sendMessage(to, "This is a test message");
   window.connectManager.sendMessage(to, { "message" : "This is a JSON test message" });

   window.connectManager.broadcastMessage("This is a test message");
   window.connectManager.broadcastMessage({ "message" : "This is a JSON test message" });
