Subscription
============

Subscription objects are returned when calling capability subscription
methods.

Subscription objects allow listening for success/error events from the
request. Success events may be emitted multiple times when updates to
the subscription are received.

Example:

.. code-block:: javascript

   var subscription = device.getVolumeControl().subscribeVolume();
   var updateCount = 0;

   subscription.success(function (volume) {
       // this may be called multiple times
       console.log("got volume update: " + volume);

       updateCount++;
       if (updateCount > 5) {
           // unsubscribe after 5 updates
           subscription.unsubscribe();
       }
   }).error(function (err) {
       console.error("subscription failed");
   });

Methods
-------

subscription.\ **unsubscribe** ()
   Unsubscribes from this subscription. Notifies the device that updates
   are no longer needed, and stops emitting events from this
   Subscription object.

Mixin Methods - SimpleEventEmitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

subscription.\ **addListener** (*event*, *callback*, [*context*])
   Add event listener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

subscription.\ **removeListener** (*event*, [*callback*], [*context*])
   Remove event listener with the specified callback and context. If
   callback is null or undefined, all callbacks for this event will be
   removed.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) [optional] – function originally passed to addListener

   -  context (object) [optional] – context object originally passed to addListener

   **Returns:** object – reference to the same object to allow chaining

subscription.\ **on** (*event*, *callback*, [*context*])
   Alias for addListener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

subscription.\ **off** (*event*, [*callback*], [*context*])
   Alias for removeListener.

   **Parameters:**

   -  event (string) – event name

   -  callback (function) [optional] – function originally passed to on

   -  context (object) [optional] – context object originally passed to on

   **Returns:** object – reference to the same object to allow chaining

Mixin Methods - SuccessCallbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

subscription.\ **success** (*callback*, [*context*])
   Register a callback for the "success" event. The success callback may
   be called with zero or more arguments depending on the type of
   response.

   Example:

   .. code-block:: javascript

      obj.success(function (result) {
          this.report("I got a result: " + result);
      }, this);

   **Parameters:**

   -  callback (function) – function to call when event is fired

   -  context (*) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

subscription.\ **error** (*callback*, [*context*])
   Register a callback for the "error" event. The error callback will be
   called with a error object as the only argument.

   Example:

   .. code-block:: javascript

      obj.error(function (err) {
          this.reportError("I got an error: " + err);
      }, this);

   **Parameters:**

   -  callback (function) – function to call when event is fired

   -  context (*) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

subscription.\ **complete** (*callback*, [*context*])
   Register a callback for the "complete" event. The complete callback
   will be called with

   Example:

   .. code-block:: javascript

      obj.complete(function (err, result) {
          if (err) {
              this.report("I got an error: " + err);
          } else {
              console.log("I got a result: " + result);
          }
      }, this);

   **Parameters:**

   -  callback (function) – function to call when event is fired

   -  context (*) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining
