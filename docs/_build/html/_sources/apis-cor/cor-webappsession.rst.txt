WebAppSession
=============

A WebAppSession represents a web-based app running on a TV. You can
communicate with a web app by first calling connect() to establish a
communication channel, and then listening for "message" events as well
as sending your own messages using sendText and sendJSON.

Example:

.. code-block:: javascript

   device.getWebAppLauncher().launchWebApp(webAppId).success(function (session) {
       this.session = session.acquire(); // hold on to a reference

       session.connect().success(function () {
           session.sendText("Hello world");
       });

       session.on('message', function (message) {
           // message could be either a string or an object
           if (typeof message === 'string') {
               console.log("received string message: " + message);
           } else {
               console.log("received object message: " + JSON.stringify(message);
           }
       }, this);

       session.on('disconnect', function () {
           console.log("session disconnected");
           this.session = null;
       }, this);

   }, this);

Methods
-------

webAppSession.\ **connect** ()
   Open a message channel to the app.

   **Returns:** :doc:`Command <cor-command>`

webAppSession.\ **disconnect** ()
   Close channel to app.

   **Returns:** :doc:`Command <cor-command>`

webAppSession.\ **setWebAppSessionListener** ()
   Set web app session listener to app

   **Returns:** :doc:`Command <cor-command>`

webAppSession.\ **sendText** (*text*)
   Send a text string to the app. Must be connected first.

   **Parameters:**

   -  text (string) – Text to send to the app

   **Returns:** :doc:`Command <cor-command>`

webAppSession.\ **sendJSON** (*object*)
   Send a plain JavaScript object to the app. Must be connected first.
   If the receiving app does not support non-string messages, the object
   will be serialized into a string in JSON format.

   **Parameters:**

   -  object (object) – Plain JavaScript object to send to the app

   **Returns:** :doc:`Command <cor-command>`

webAppSession.\ **close** ()
   Close the web app.

   **Returns:** :doc:`Command <cor-command>`

Mixin Methods - SimpleEventEmitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

webAppSession.\ **addListener** (*event*, *callback*, [*context*])
   Add event listener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

webAppSession.\ **removeListener** (*event*, [*callback*], [*context*])
   Remove event listener with the specified callback and context. If
   callback is null or undefined, all callbacks for this event will be
   removed.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) [optional] – function originally passed to addListener

   -  context (object) [optional] – context object originally passed to addListener

   **Returns:** object – reference to the same object to allow chaining

webAppSession.\ **on** (*event*, *callback*, [*context*])
   Alias for addListener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

webAppSession.\ **off** (*event*, [*callback*], [*context*])
   Alias for removeListener.

   **Parameters:**

   -  event (string) – event name

   -  callback (function) [optional] – function originally passed to on

   -  context (object) [optional] – context object originally passed to on

   **Returns:** object – reference to the same object to allow chaining

Mixin Methods - WrappedObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

webAppSession.\ **acquire** ()
   Indicate that you would like to keep an active reference to this
   object. Wrapped objects that are not acquired may be freed after the
   success callback returns.

   **Returns:** object – reference to object

webAppSession.\ **release** ()
   Release the reference to this object. After calling .release(), this
   object may no longer be used. You should always release objects when
   you no longer need them, to avoid memory leaks.
