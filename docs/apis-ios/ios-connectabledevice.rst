ConnectableDevice
=================

Overview
--------

ConnectableDevice serves as a normalization layer between your app and
each of the device's services. It consolidates a lot of key data about
the physical device and provides access to underlying functionality.

In Depth
--------

ConnectableDevice consolidates some key information about the physical
device, including model name, friendly name, ip address, connected
DeviceService names, etc. In some cases, it is not possible to
accurately select which DeviceService has the best friendly name, model
name, etc. In these cases, the values of these properties are dependent
upon the order of DeviceService discovery.

To be informed of any ready/pairing/disconnect messages from each of the
DeviceService, you must set a delegate.

ConnectableDevice exposes capabilities that exist in the underlying
DeviceServices such as TV Control, Media Player, Media Control, Volume
Control, etc. These capabilities, when accessed through the
ConnectableDevice, will be automatically chosen from the most suitable
DeviceService by using that DeviceService's CapabilityPriorityLevel.

Properties
----------

id<:doc:`ConnectableDeviceDelegate <ios-connectabledevicedelegate>` > delegate
   Delegate which should receive messages on certain events.

NSString \* id
   Universally unique ID of this particular ConnectableDevice object,
   persists between sessions in ConnectableDeviceStore for connected
   devices

NSString \* address
   Current IP address of the ConnectableDevice.

NSString \* friendlyName
   An estimate of the ConnectableDevice's current friendly name.

NSString \* modelName
   An estimate of the ConnectableDevice's current model name.

NSString \* modelNumber
   An estimate of the ConnectableDevice's current model number.

NSString \* lastKnownIPAddress
   Last IP address this ConnectableDevice was discovered at.

NSString \* lastSeenOnWifi
   Name of the last wireless network this ConnectableDevice was
   discovered on.

double lastConnected
   Last time (in seconds from 1970) that this ConnectableDevice was
   connected to.

double lastDetection
   Last time (in seconds from 1970) that this ConnectableDevice was
   detected.

BOOL isConnectable
   Whether the device has any DeviceServices that require an active
   connection (websocket, HTTP registration, etc)

BOOL connected
   Whether all the DeviceServices are connected.

NSArray \* services
   Array of all currently discovered DeviceServices this
   ConnectableDevice has associated with it.

BOOL hasServices
   Whether the ConnectableDevice has any running DeviceServices
   associated with it.

NSArray \* capabilities
   A combined list of all capabilities that are supported among the
   detected DeviceServices.

Methods
-------

\- (void) **connect**
   Enumerates through all DeviceServices and attempts to connect to each
   of them. When all of a ConnectableDevice's DeviceServices are ready
   to receive commands, the ConnectableDevice will send a
   connectableDeviceReady: message to its delegate.

   It is always necessary to call connect on a ConnectableDevice, even
   if it contains no connectable DeviceServices.

\- (void) **disconnect**
   Enumerates through all DeviceServices and attempts to disconnect from
   each of them.

\- (void) **addService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   Adds a DeviceService to the ConnectableDevice instance. Only one
   instance of each DeviceService type (webOS, Netcast, etc) may be
   attached to a single ConnectableDevice instance. If a device contains
   your service type already, your service will not be added.

   **Parameters:**

   * service – DeviceService to be added to the ConnectableDevice

\- (void) **removeServiceWithId**:(NSString \*)\ *serviceId*
   Removes a DeviceService from the ConnectableDevice instance.
   serviceId is used as the identifier because only one instance of each
   DeviceService type may be attached to a single ConnectableDevice
   instance.

   **Parameters:**

   * serviceId – Id of the DeviceService to be removed from the ConnectableDevice

\- (:doc:`DeviceService <ios-deviceservice>` \*) **serviceWithName**:(NSString \*)\ *serviceId*
   Obtains a service from the device with the provided serviceId

   **Parameters:**

   * serviceId – Service ID of the targeted DeviceService (webOS, Netcast, DLNA, etc)

   **Returns:** DeviceService with the specified serviceId or nil, if none exists

\- (BOOL) **hasCapability**:(NSString \*)\ *capability*
   Test to see if the capabilities array contains a given capability.
   See the individual Capability classes for acceptable capability
   values.

   It is possible to append a wildcard search term ``.Any`` to the end
   of the search term. This method will return true for capabilities
   that match the term up to the wildcard.

   Example: ``Launcher.App.Any``

   **Parameters:**

   * capability – Capability to test against

\- (BOOL) **hasCapabilities**:(NSArray \*)\ *capabilities*
   Test to see if the capabilities array contains a given set of
   capabilities. See the individual Capability classes for acceptable
   capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   **Parameters:**

   * capabilities – Array of capabilities to test against

\- (BOOL) **hasAnyCapability**:(NSArray \*)\ *capabilities*
   Test to see if the capabilities array contains at least one
   capability in a given set of capabilities. See the individual
   Capability classes for acceptable capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   **Parameters:**

   * capabilities – Array of capabilities to test against

\- (void) **setPairingType**:(:doc:`DeviceServicePairingType <ios-deviceservicepairingtype>`)\ *pairingType*
   Set the type of pairing for the ConnectableDevice services. By
   default the value will be DeviceServicePairingTypeNone

   For WebOSTV's If pairingType is set to
   DeviceServicePairingTypeFirstScreen(default), the device will prompt
   the user to pair when connecting to the ConnectableDevice.

   If pairingType is set to DeviceServicePairingTypePinCode, the device
   will prompt the user to enter a pin to pair when connecting to the
   ConnectableDevice.

   **Parameters:**

   * pairingType – value to be set for the device service from DeviceServicePairingType

\- (id<:doc:`Launcher <ios-launcher>` >) **launcher**

\- (id<:doc:`ExternalInputControl <ios-externalinputcontrol>` >) **externalInputControl**
   Accessor for highest priority Launcher object

\- (id<:doc:`MediaPlayer <ios-mediaplayer>` >) **mediaPlayer**
   Accessor for highest priority ExternalInputControl object

\- (id<:doc:`MediaControl <ios-mediacontrol>` >) **mediaControl**
   Accessor for highest priority MediaPlayer object

\- (id<:doc:`VolumeControl <ios-volumecontrol>` >) **volumeControl**
   Accessor for highest priority MediaControl object

\- (id<:doc:`TVControl <ios-tvcontrol>` >) **tvControl**
   Accessor for highest priority VolumeControl object

\- (id<:doc:`KeyControl <ios-keycontrol>` >) **keyControl**
   Accessor for highest priority TVControl object

\- (id<:doc:`TextInputControl <ios-textinputcontrol>` >) **textInputControl**
   Accessor for highest priority KeyControl object

\- (id<:doc:`MouseControl <ios-mousecontrol>` >) **mouseControl**
   Accessor for highest priority TextInputControl object

\- (id<:doc:`PowerControl <ios-powercontrol>` >) **powerControl**
   Accessor for highest priority MouseControl object

\- (id<:doc:`ToastControl <ios-toastcontrol>` >) **toastControl**
   Accessor for highest priority PowerControl object

\- (id<:doc:`WebAppLauncher <ios-webapplauncher>` >) **webAppLauncher**
   Accessor for highest priority ToastControl object
