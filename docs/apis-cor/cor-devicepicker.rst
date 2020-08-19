DevicePicker
============

DevicePicker represents a picker UI widget created by calling
``DiscoveryManager.pickDevice()``.

Example:

.. code-block:: javascript

   var devicePicker = ConnectSDK.discoveryManager.pickDevice()
   devicePicker.success(function (device) {
       console.log("picked device " + device.getFriendlyName());
   });

Methods
-------

devicePicker.\ **close** ()
   Close the device picker.

Mixin Methods - SimpleEventEmitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

devicePicker.\ **addListener** (*event*, *callback*, [*context*])
   Add event listener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

devicePicker.\ **removeListener** (*event*, [*callback*], [*context*])
   Remove event listener with the specified callback and context. If
   callback is null or undefined, all callbacks for this event will be
   removed.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) [optional] – function originally passed to addListener

   -  context (object) [optional] – context object originally passed to addListener

   **Returns:** object – reference to the same object to allow chaining

devicePicker.\ **on** (*event*, *callback*, [*context*])
   Alias for addListener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

devicePicker.\ **off** (*event*, [*callback*], [*context*])
   Alias for removeListener.

   **Parameters:**

   -  event (string) – event name

   -  callback (function) [optional] – function originally passed to on

   -  context (object) [optional] – context object originally passed to on

   **Returns:** object – reference to the same object to allow chaining

Mixin Methods - SuccessCallbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

devicePicker.\ **success** (*callback*, [*context*])
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

devicePicker.\ **error** (*callback*, [*context*])
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

devicePicker.\ **complete** (*callback*, [*context*])
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
