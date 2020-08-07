FireTVService
=============

*extends* :doc:`DeviceService <ios-deviceservice>`

``FireTVService`` provides capabilities for Amazon Fire TV and Fire TV
Stick devices. ``FireTVService`` acts a layer on top of Amazon's Fling
SDK, and requires the Fling SDK framework to function. ``FireTVService``
provides the following functionality:

* Media playback

* Media control

Using Connect SDK for discovery/control of Fire TV devices will result in your app complying with the Amazon Fling SDK terms of service.

Properties
----------

id<:doc:`BlockRunner <ios-blockrunner>`> delegateBlockRunner
   The ``BlockRunner`` instance specifying where to run delegate
   callbacks. The default value is the main dispatch queue runner.
   Cannot be ``nil``, as it will reset to the default value.

FireTVMediaPlayer \* fireTVMediaPlayer
   Object that controls ``MediaPlayer`` functionality.

FireTVMediaControl \* fireTVMediaControl
   Object that controls ``MediaControl`` functionality.

id<RemoteMediaPlayer> remoteMediaPlayer
   A ``RemoteMediaPlayer`` that's controlled by this service instance.
   It's returned from the ``ServiceDescription`` object, and thus can be
   ``nil`` if the ``serviceDescription`` property is ``nil``.

:doc:`AppStateChangeNotifier <ios-appstatechangenotifier>` \* appStateChangeNotifier
   An ``AppStateChangeNotifier`` that allows to track app state changes.

Methods
-------

\- (instancetype) **initWithAppStateChangeNotifier**:(nullable :doc:`AppStateChangeNotifier <ios-appstatechangenotifier>` \*)\ *stateNotifier*
   Initializes the instance with the given ``AppStateChangeNotifier``.
   Using ``nil`` parameter will create real object.

   **Parameters:**

   * stateNotifier

Inherited Methods
-----------------

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

   * pairingData – Data to be used for pairing. The type of this parameter will vary depending on what type of pairing is required, but is likely to be a string (pin code, pairing key, etc).

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
