CastService
===========

*extends* :doc:`DeviceService <ios-deviceservice>`

CastService provides capabilities for Google Chromecast devices.
CastService acts as a layer on top of Google's own Cast SDK, and
requires the Cast SDK library to function. CastService provides the
following functionality:

* Media playback
* Media control
* Web app launching & two-way communication
* Volume control

Using Connect SDK for discovery/control of Chromecast devices will
result in your app complying with the Google Cast SDK `terms of
service <https://developers.google.com/cast/docs/terms>`__.

To learn more about Cast SDK, visit the `Google Cast SDK Developer
site <https://developers.google.com/cast/>`__.

Properties
----------

GCKDeviceManager \* castDeviceManager
   The GCKDeviceManager that CastService is using internally to manage
   devices.

GCKDevice \* castDevice
   The GCKDevice object that CastService is using internally for device
   information.

CastServiceChannel \* castServiceChannel
   The CastServiceChannel is used for app-to-app communication that is
   handling by the Connect SDK JavaScript Bridge.

GCKMediaControlChannel \* castMediaControlChannel
   The GCKMediaControlChannel that the CastService is using to send
   media events to the connected web app.

NSString \* castWebAppId
   The CastService will launch the specified web app id.

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
