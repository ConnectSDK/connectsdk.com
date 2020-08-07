DeviceService
=============

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
set the DeviceService's delegate to the ConnectableDevice that owns the
DeviceService. You should not change the delegate unless you intend to
manage the lifecycle of that service. The DeviceService will proxy all
of its delegate method calls through the ConnectableDevice's
ConnectableDeviceDelegate.

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

Properties
----------

id<:doc:`DeviceServiceDelegate <ios-deviceservicedelegate>`> delegate
   Delegate object to receive DeviceService status messages. See note in
   the "In Depth" section about changing the DeviceServiceDelegate.

ServiceDescription \* serviceDescription
   Object containing the discovered information about this DeviceService

ServiceConfig \* serviceConfig
   Object containing persistence data about this DeviceService (pairing
   info, SSL certificates, etc)

NSString \* serviceName
   Name of the DeviceService (webOS, Chromecast, etc)

NSArray \* capabilities
   An array of capabilities supported by the DeviceService. This array
   may change based off a number of factors.

   * DiscoveryManager's pairingLevel value
   * Connect SDK framework version
   * First screen device OS version
   * First screen device configuration (apps installed, settings, etc)
   * Physical region

BOOL connected
   Whether the DeviceService is currently connected

BOOL isConnectable
   Whether the DeviceService requires an active connection or
   registration process

BOOL requiresPairing
   Whether the DeviceService requires pairing or not.

:doc:`DeviceServicePairingType <ios-deviceservicepairingtype>` pairingType
   Type of pairing that this DeviceService requires. May be unknown
   until you try to connect.

id pairingData
   May contain useful information regarding pairing (pairing key length,
   etc)

Methods
-------

\+ (NSDictionary \*) **discoveryParameters**
   A dictionary of keys/values that will be used by the
   DiscoveryProvider used to discover this DeviceService. Some keys that
   are used are: service name, SSDP filter, etc.

\+ (:doc:`DeviceService <ios-deviceservice>` \*) **deviceServiceWithClass**:(Class)\ *\_class* **serviceConfig**:(ServiceConfig \*)\ *serviceConfig*
   **Parameters:**

   * \_class
   * **serviceConfig**: serviceConfig

\+ (BOOL) **shouldDisconnectOnBackground**
   Static property that determines whether a DeviceService subclass
   should shut down communication channels when the app enters a
   background state. This may be helpful for apps that need to
   communicate with web apps from the background. This property may not
   be applicable to all DeviceService subclasses.

   Sets the shouldDisconnectOnBackground static property. This property
   should be set before starting DiscoveryManager for the first time.

\+ (void) **setShouldDisconnectOnBackround**:(BOOL)\ *shouldDisconnectOnBackground*
   **Parameters:**

   * shouldDisconnectOnBackground

\- (instancetype) **initWithServiceConfig**:(ServiceConfig \*)\ *serviceConfig*
   **Parameters:**

   * serviceConfig

\- (BOOL) **hasCapability**:(NSString \*)\ *capability*
   **Parameters:**

   * capability

\- (BOOL) **hasCapabilities**:(NSArray \*)\ *capabilities*
   **Parameters:**

   * capabilities

\- (BOOL) **hasAnyCapability**:(NSArray \*)\ *capabilities*
   **Parameters:**

   * capabilities

\- (void) **connect**
   Will attempt to connect to the DeviceService. The failure/success
   will be reported back to the DeviceServiceDelegate. If the connection
   attempt reveals that pairing is required, the DeviceServiceDelegate
   will also be notified in that event.

\- (void) **disconnect**
   Will attempt to disconnect from the DeviceService. The
   failure/success will be reported back to the DeviceServiceDelegate.

\- (void) **pairWithData**:(id)\ *pairingData*
   Will attempt to pair with the DeviceService with the provided
   pairingData. The failure/success will be reported back to the
   DeviceServiceDelegate.

   **Parameters:**

   * pairingData –

      Data to be used for pairing. The type of this parameter will vary
      depending on what type of pairing is required, but is likely to be
      a string (pin code, pairing key, etc).

\- (void) **closeLaunchSession**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Every LaunchSession object has an associated DeviceService.
   Internally, LaunchSession's close method proxies to it's
   DeviceService's closeLaunchSession method. If, for some reason, your
   LaunchSession loses it's DeviceService reference, you can call this
   closeLaunchSession method directly.

   **Parameters:**

   * launchSession – LaunchSession to be closed
   * **success**: success – (optional) SuccessBlock to be called on success
   * **failure**: failure – (optional) FailureBlock to be called on failure
