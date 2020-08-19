WebOSTVService
==============

*extends*\ :doc:`DeviceService <ios-deviceservice>`

WebOSTVService provides capabilities for LG Smart TVs running webOS
(model year 2014). The second screen gateway running on the webOS
provides different capabilities based on whether pairing is enabled or
not.

-  Web app launching & two-way communication
-  App launching
-  Media playback
-  Media control
-  Volume control
-  Text input control\*
-  Key control (fiveway)\*
-  Mouse control\*
-  Power control\*
-  TV control (change channels, get channel info)\*
-  External input control\*
-  Toast control\*

\* = requires pairing

Commands & subscriptions on webOS occur over a WebSocket connection.

webOS Version History
---------------------

The following version numbers represent the version of webOS released
for LG Smart TVs. The version numbers are associated with any changes to
the platform's second screen APIs in that particular version.

4.0.0

-  Initial release

4.0.1

-  No changes

4.0.2

-  Added app-to-app support
-  Added the ability to request pin or prompt pairing

4.0.3

-  Fixed a subscription bug in app-to-app

Inherited Methods
-----------------

\+ (NSDictionary \*) **discoveryParameters**
   A dictionary of keys/values that will be used by the
   DiscoveryProvider used to discover this DeviceService. Some keys that
   are used are: service name, SSDP filter, etc.

\+ (:doc:`DeviceService <ios-deviceservice>` \*) **deviceServiceWithClass**:(Class)\ *\_class* **serviceConfig**:(ServiceConfig \*)\ *serviceConfig*
   **Parameters:**

   -  \_class
   -  **serviceConfig**: serviceConfig

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

   -  shouldDisconnectOnBackground

\- (instancetype) **initWithServiceConfig**:(ServiceConfig \*)\ *serviceConfig*
   **Parameters:**

   -  serviceConfig

\- (BOOL) **hasCapability**:(NSString \*)\ *capability*
   **Parameters:**

   -  capability

\- (BOOL) **hasCapabilities**:(NSArray \*)\ *capabilities*
   **Parameters:**

   -  capabilities

\- (BOOL) **hasAnyCapability**:(NSArray \*)\ *capabilities*
   **Parameters:**

   -  capabilities

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

   -  pairingData – Data to be used for pairing. The type of this parameter will vary
      depending on what type of pairing is required, but is likely to be
      a string (pin code, pairing key, etc).

\- (void) **closeLaunchSession**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Every LaunchSession object has an associated DeviceService.
   Internally, LaunchSession's close method proxies to it's
   DeviceService's closeLaunchSession method. If, for some reason, your
   LaunchSession loses it's DeviceService reference, you can call this
   closeLaunchSession method directly.

   **Parameters:**

   -  launchSession – LaunchSession to be closed

   -  **success**: success – (optional) SuccessBlock to be called on success

   -  **failure**: failure – (optional) FailureBlock to be called on failure
