DeviceService com.connectsdk.service.DeviceService
==================================================

Overview
--------

From a high-level perspective, DeviceService completely abstracts the
functionality of a particular service/protocol (webOS TV, Netcast TV,
Chromecast, Roku, DIAL, etc).

In Depth
--------

DeviceService is an abstract class that is meant to be extended. You
shouldn't ever use DeviceService directly, unless extending it to
provide support for an additional service/protocol.

Immediately after discovery of a DeviceService, DiscoveryManager will
set the DeviceService's Listener to the ConnectableDevice that owns the
DeviceService. You should not change the Listener unless you intend to
manage the lifecycle of that service. The DeviceService will proxy all
of its Listener method calls through the ConnectableDevice's
ConnectableDeviceListener.

Connection & Pairing
~~~~~~~~~~~~~~~~~~~~

Your ConnectableDevice object will let you know if you need to connect
or pair to any services.

Capabilities
~~~~~~~~~~~~

All DeviceService objects have a group of capabilities. These
capabilities can be implemented by any object, and that object will be
returned when you call the DeviceService's capability methods (launcher,
mediaPlayer, volumeControl, etc).

Inner Classes
-------------

-  `DeviceServiceListener </apis/1-6-0/android/DeviceServiceListener>`__
-  `PairingType </apis/1-6-0/android/PairingType>`__

Methods
-------

void **connect** ()
   Will attempt to connect to the DeviceService. The failure/success
   will be reported back to the DeviceServiceListener. If the connection
   attempt reveals that pairing is required, the DeviceServiceListener
   will also be notified in that event.

void **disconnect** ()
   Will attempt to disconnect from the DeviceService. The
   failure/success will be reported back to the DeviceServiceListener.

boolean **isConnected** ()
   Whether the DeviceService is currently connected

boolean **isConnectable** ()

void **cancelPairing** ()
   Explicitly cancels pairing in services that require pairing. In some
   services, this will hide a prompt that is displaying on the device.

void **sendPairingKey** (String *pairingKey*)
   Will attempt to pair with the DeviceService with the provided
   pairingData. The failure/success will be reported back to the
   DeviceServiceListener.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  pairingKey –

      Data to be used for pairing. The type of this parameter will vary
      depending on what type of pairing is required, but is likely to be
      a string (pin code, pairing key, etc).

List<String> **getCapabilities** ()

boolean **hasCapability** (String *capability*)
   Test to see if the capabilities array contains a given capability.
   See the individual Capability classes for acceptable capability
   values.

   It is possible to append a wildcard search term ``.Any`` to the end
   of the search term. This method will return true for capabilities
   that match the term up to the wildcard.

   Example: ``Launcher.App.Any``

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  capability –

      Capability to test against

boolean **hasAnyCapability** (String... *capabilities*)
   Test to see if the capabilities array contains at least one
   capability in a given set of capabilities. See the individual
   Capability classes for acceptable capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  capabilities –

      Set of capabilities to test against

boolean **hasCapabilities** (List<String> *capabilities*)
   Test to see if the capabilities array contains a given set of
   capabilities. See the individual Capability classes for acceptable
   capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  capabilities –

      List of capabilities to test against

boolean **hasCapabilities** (String... *capabilities*)
   Test to see if the capabilities array contains a given set of
   capabilities. See the individual Capability classes for acceptable
   capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  capabilities –

      Set of capabilities to test against

ServiceDescription **getServiceDescription** ()

ServiceConfig **getServiceConfig** ()

JSONObject **toJSONObject** ()

String **getServiceName** ()
   Name of the DeviceService (webOS, Chromecast, etc)

void **closeLaunchSession** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Closes the session on the first screen device. Depending on the
   sessionType, the associated service will have different ways of
   handling the close functionality.

   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  launchSession –

      LaunchSession to close

   -  listener –

      (optional) listener to be called on success/failure

Inherited Methods
-----------------

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
   .. rubric:: Parameters:
      :name: parameters-8
      :class: method-detail-label

   -  command
