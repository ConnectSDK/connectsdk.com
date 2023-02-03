ConnectableDevice
=================

ConnectableDevice represents a device on the network. It provides
several *capability interfaces* which allow the developer to get
information from and control the device.

These interfaces are accessed using getter methods like
device.getLauncher(). Not all of the capabilities or methods are
available on every device; you should check if the functionality is
supported using device.supports(capabilityName).

If the device was selected from the built-in picker, it will already be
connected; if the device was obtained from elsewhere then you must call
device.connect() and wait for the "ready" event before trying to use the
device.

Example:

.. code-block:: javascript

   device.on("ready", function () {
       // ready to send commands now
       device.getLauncher().launchYouTube(videoId);
   });

   device.connect();

ConnectableDevice emits the following high-level events:

-  ready - device is ready to use
-  disconnect - device is no longer connected
-  capabilitieschanged - some capabilities may be available or
   unavailable now

Internally, ConnectableDevice uses one or more *services* to control a
device on the network. Services speak a specific protocol like DIAL or
DLNA or other vendor-specific protocols. Services are not directly
accessible from the Connect SDK Cordova plugin at this time.

There are several events related to the process of connecting to
individual services:

-  serviceconnectionrequired - pending connection
-  serviceconnectionerror - error connecting to a service
-  servicepairingrequired - pairing is required for a service
-  servicepairingsuccess - pairing successful for a service
-  servicepairingerror - error pairing with a service

Methods
-------

connectableDevice.\ **getLauncher** ()
   **Returns:** :doc:`Launcher <cor-launcher>`

connectableDevice.\ **getMediaPlayer** ()
   **Returns:** :doc:`MediaPlayer <cor-mediaplayer>`

connectableDevice.\ **getExternalInputControl** ()
   **Returns:** :doc:`ExternalInputControl <cor-externalinputcontrol>`

connectableDevice.\ **getMediaControl** ()
   **Returns:** :doc:`MediaControl <cor-mediacontrol>`

connectableDevice.\ **getKeyControl** ()
   **Returns:** :doc:`KeyControl <cor-keycontrol>`

connectableDevice.\ **getMouseControl** ()
   **Returns:** :doc:`MouseControl <cor-mousecontrol>`

connectableDevice.\ **getTextInputControl** ()
   **Returns:** :doc:`TextInputControl <cor-textinputcontrol>`

connectableDevice.\ **getPowerControl** ()
   **Returns:** :doc:`PowerControl <cor-powercontrol>`

connectableDevice.\ **getToastControl** ()
   **Returns:** :doc:`ToastControl <cor-toastcontrol>`

connectableDevice.\ **getTVControl** ()
   **Returns:** :doc:`TVControl <cor-tvcontrol>`

connectableDevice.\ **getVolumeControl** ()
   **Returns:** :doc:`VolumeControl <cor-volumecontrol>`

connectableDevice.\ **getWebAppLauncher** ()
   **Returns:** :doc:`WebAppLauncher <cor-webapplauncher>`

connectableDevice.\ **connect** ()
   Connect to the device.

connectableDevice.\ **disconnect** ()
   Disconnect from the device.

connectableDevice.\ **setPairingType** (*pairingType*)
   Set a desirable pairing type to the device.

   **Parameters:**

   -  pairingType – (string): PairingType to use

connectableDevice.\ **isReady** ()
   Returns true if device is ready to use.

connectableDevice.\ **getFriendlyName** ()
   Get the human-readable name of the device.

   **Returns:** string

connectableDevice.\ **getIPAddress** ()
   Get the last known IP address of the device.

   **Returns:** string

connectableDevice.\ **getModelName** ()
   Get the device model name.

   **Returns:** string

connectableDevice.\ **getModelNumber** ()
   Get the device model number.

   **Returns:** string

connectableDevice.\ **getCapabilities** ()
   Get a list of capabilities supported by this device.

   **Returns:** string[] – array of capabilities supported by this device

connectableDevice.\ **hasCapability** (*name*)
   **Parameters:**

   -  name (string) – of capability. You should use the ConnectSDK.Capabilities constant
      to reference strings.

   **Returns:** boolean – true if device supports the given capability

connectableDevice.\ **supports** ([*...*])
   Flexible version of hasCapability which returns true if all of the
   capabilities specified are supported.

   -  supports(ConnectSDK.Capabilities.MediaControl.Any)
   -  supports(ConnectSDK.Capabilities.VolumeControl.Set,
      ConnectSDK.Capabilities.Launcher.Any)
   -  supports([ConnectSDK.Capabilities.TVControl.Any,
      ConnectSDK.Capabilities.Launcher.Any])

   **Parameters:**

   -  ... [optional] – array of capability names. You should use the
      ConnectSDK.Capabilities constant to reference strings.

   **Returns:** boolean – true if all specified capabilities are supported

connectableDevice.\ **supportsAny** ([*...*])
   Like supports() but returns true if any specified capability is
   supported.

   **Parameters:**

   -  ... [optional] – array of capability names. You should use the
      ConnectSDK.Capabilities constant to reference strings.

   **Returns:** boolean – true if any specified capability is supported

connectableDevice.\ **hasService** (*serviceName*)
   Returns true if the device supports the specified service. See
   ConnectSDK.Services for a list of constants.

   **Parameters:**

   -  serviceName (string)

   **Returns:** boolean – true if service is supported

connectableDevice.\ **getService** (*serviceName*)
   Returns a wrapper for a service which gives access to low-level
   functionality. Only a limited subset of the services supported by the
   native SDK are available through this plugin.

   **Parameters:**

   -  serviceName (string)

   **Returns:** object – service object or null if not supported

connectableDevice.\ **getId** ()
   Returns an internal id assigned by the SDK to this device. For
   devices that have been connected to or paired, this id will be
   persisted to disk in the device store to allow the app to identify
   the device later (such as reconnecting to the last connected device
   when starting the app).

Mixin Methods - SimpleEventEmitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

connectableDevice.\ **addListener** (*event*, *callback*, [*context*])
   Add event listener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

connectableDevice.\ **removeListener** (*event*, [*callback*], [*context*])
   Remove event listener with the specified callback and context. If
   callback is null or undefined, all callbacks for this event will be
   removed.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) [optional] – function originally passed to addListener

   -  context (object) [optional] – context object originally passed to addListener

   **Returns:** object – reference to the same object to allow chaining

connectableDevice.\ **on** (*event*, *callback*, [*context*])
   Alias for addListener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

connectableDevice.\ **off** (*event*, [*callback*], [*context*])
   Alias for removeListener.

   **Parameters:**

   -  event (string) – event name

   -  callback (function) [optional] – function originally passed to on

   -  context (object) [optional] – context object originally passed to on

   **Returns:** object – reference to the same object to allow chaining
