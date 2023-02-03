Port a Receiver App to webOS
============================

The Connect SDK JavaScript Bridge has been designed to enable near
feature-parity with existing platforms. Ideally, one web app should be
capable of running across the range of TV platforms available on the
market.

This article will take a Custom "Receiver" developed for Chromecast and
port it to work on both webOS and Chromecast through Connect SDK.

Here is the code for the Chromecast-specific app.

.. code-block:: html

   <!doctype html>
   <html>
   <head>
       <title>Chromecast Custom Receiver</title>
   </head>
   <body>
       <video id='media' />
       <script src="//www.gstatic.com/cast/sdk/libs/receiver/2.0.0/cast_receiver.js"></script>
       <script>
           window.onload = function() {
               window.mediaElement = document.getElementById('media');
               window.mediaManager = new cast.receiver.MediaManager(window.mediaElement);

               window.castReceiverManager = cast.receiver.CastReceiverManager.getInstance();

               window.castMessageBus = window.castReceiverManager.getCastMessageBus("urn:x-cast:com.example.MyApp");
               window.castMessageBus.addEventListener("message", function(message) {
                   window.castMessageBus.broadcast("Got your message");
               });

               window.castReceiverManager.start();
           };
       </script>
   </body>
   </html>

There are a few things happening here.

#. The Chromecast SDK is being loaded
#. On page load, Chromecast SDK is being initialized
#. While initializing Chromecast, it is given a reference to our media
   element
#. A channel for communication is being established with a response on
   each message received
#. Event listeners are being added to the media element to track play
   state

With the Connect SDK JavaScript Bridge, these steps remain very similar.

#. This Chromecast SDK is being loaded
#. The Connect SDK JavaScript Bridge is being loaded
#. On page load, Connect SDK is being initialized
#. While initializing Connect SDK, it is given a reference to our media
   element
#. A channel for communication is being established with a response on
   each message received
#. Event listeners are being added to the media element to track play
   state

See the Connect SDK implementation below.

.. code-block:: html

   <!doctype html>
   <html>
   <head>
       <title>Connect SDK Web App</title>
   </head>
   <body>
       <video id='media' />
       <script src="//www.gstatic.com/cast/sdk/libs/receiver/2.0.0/cast_receiver.js"></script>
       <script src="connectsdk.js"></script>
       <script>
           window.onload = function() {
               window.connectManager = new connectsdk.ConnectManager();

               window.mediaElement = document.getElementById('media');
               window.connectManager.setMediaElement(window.mediaElement);

               window.connectManager.on("message", function(data) {
                   window.connectManager.sendMessage(data.from, "Got your message");
               });

               window.connectManager.init();
           };
       </script>
   </body>
   </html>

In this basic example, we were able to port an app from one platform to
two by only adding one line of code (a JavaScript file import). Under
the hood, the Connect SDK JavaScript bridge will run the initialization
for whichever platform it is detected as running on.

We encourage you to attach media events directly to your media element
to avoid having to add platform-specific code to your web app.

--------------

*Portions of this page are modifications based on work created
and* \ `shared by
Google <https://developers.google.com/readme/policies/>`__\  *and used
according to terms described in the* \ `Creative Commons 3.0 Attribution
License <http://creativecommons.org/licenses/by/3.0/>`__\ *.*
