ConnectableDevice
==================
``com.connectsdk.device.ConnectableDevice``

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
DeviceService, you must set a listener.

ConnectableDevice exposes capabilities that exist in the underlying
DeviceServices such as TV Control, Media Player, Media Control, Volume
Control, etc. These capabilities, when accessed through the
ConnectableDevice, will be automatically chosen from the most suitable
DeviceService by using that DeviceService's CapabilityPriorityLevel.

Methods
-------

void **setPairingType** (:doc:`PairingType <and-pairingtype>` *pairingType*)
    set desirable pairing type for all services

    **Parameters:**

    * pairingType

void **addService** (:doc:`DeviceService <and-deviceservice>` *service*)
    Adds a DeviceService to the ConnectableDevice instance. Only one
    instance of each DeviceService type (webOS, Netcast, etc) may be
    attached to a single ConnectableDevice instance. If a device contains
    your service type already, your service will not be added.

    **Parameters:**

    * service – DeviceService to be added

void **removeService** (:doc:`DeviceService <and-deviceservice>` *service*)
    Removes a DeviceService from the ConnectableDevice instance.

    **Parameters:**

    * service – DeviceService to be removed

void **removeServiceWithId** (String *serviceId*)
    Removes a DeviceService from the ConnectableDevice instance.

    **Parameters:**

    * serviceId – ID of the DeviceService to be removed (DLNA, webOS TV, etc)

Collection<:doc:`DeviceService <and-deviceservice>`> **getServices** ()
    Array of all currently discovered DeviceServices this
    ConnectableDevice has associated with it.

:doc:`DeviceService <and-deviceservice>` **getServiceByName** (String *serviceName*)
    Obtains a service from the ConnectableDevice with the provided
    serviceName

    **Parameters:**

    * serviceName – Service ID of the targeted DeviceService (webOS, Netcast, DLNA, etc)

    **Returns:** DeviceService with the specified serviceName or nil, if none exists

void **removeServiceByName** (String *serviceName*)
    Removes a DeviceService form the ConnectableDevice instance.
    serviceName is used as the identifier because only one instance of
    each DeviceService type may be attached to a single ConnectableDevice
    instance.

    **Parameters:**

    * serviceName – Name of the DeviceService to be removed from the ConnectableDevice.

:doc:`DeviceService <and-deviceservice>` **getServiceWithUUID** (String *serviceUUID*)
    Returns a DeviceService from the ConnectableDevice instance.
    serviceUUID is used as the identifier because only one instance of
    each DeviceService type may be attached to a single ConnectableDevice
    instance.

    **Parameters:**

    * serviceUUID – UUID of the DeviceService to be returned

void **addListener** (:doc:`ConnectableDeviceListener <and-connectabledevicelistener>` *listener*)
    Adds the ConnectableDeviceListener to the list of listeners for this
    ConnectableDevice to receive certain events.

    **Parameters:**

    * listener – ConnectableDeviceListener to listen to device events (connect, disconnect, ready, etc)

void **setListener** (:doc:`ConnectableDeviceListener <and-connectabledevicelistener>` *listener*)
    Clears the array of listeners and adds the provided ``listener`` to
    the array. If ``listener`` is null, the array will be empty.

    This method is deprecated. Since version 1.2.1, use
    ``ConnectableDevice::addListener(ConnectableDeviceListener listener)``
    instead

    **Parameters:**

    * listener – ConnectableDeviceListener to listen to device events (connect, disconnect, ready, etc)

void **removeListener** (:doc:`ConnectableDeviceListener <and-connectabledevicelistener>` *listener*)
    Removes a previously added ConenctableDeviceListener from the list of
    listeners for this ConnectableDevice.

    **Parameters:**

    * listener – ConnectableDeviceListener to be removed

List<:doc:`ConnectableDeviceListener <and-connectabledevicelistener>`> **getListeners** ()

void **connect** ()
    Enumerates through all DeviceServices and attempts to connect to each
    of them. When all of a ConnectableDevice's DeviceServices are ready
    to receive commands, the ConnectableDevice will send a onDeviceReady
    message to its listener.

    It is always necessary to call connect on a ConnectableDevice, even
    if it contains no connectable DeviceServices.

void **disconnect** ()
    Enumerates through all DeviceServices and attempts to disconnect from
    each of them.

boolean **isConnectable** ()
    Whether the device has any DeviceServices that require an active
    connection (websocket, HTTP registration, etc)

void **sendPairingKey** (String *pairingKey*)
    Sends a pairing key to all discovered device services.

    **Parameters:**

    * pairingKey – Pairing key to send to services.

void **cancelPairing** ()
    Explicitly cancels pairing on all services that require pairing. In
    some services, this will hide a prompt that is displaying on the
    device.

List<String> **getCapabilities** ()
    A combined list of all capabilities that are supported among the
    detected DeviceServices.

boolean **hasCapability** (String *capability*)
    Test to see if the capabilities array contains a given capability.
    See the individual Capability classes for acceptable capability
    values.

    It is possible to append a wildcard search term ``.Any`` to the end
    of the search term. This method will return true for capabilities
    that match the term up to the wildcard.

    Example: ``Launcher.App.Any``

    **Parameters:**

    * capability – Capability to test against

boolean **hasAnyCapability** (String... *capabilities*)
    Test to see if the capabilities array contains at least one
    capability in a given set of capabilities. See the individual
    Capability classes for acceptable capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**

    * capabilities – Array of capabilities to test against

boolean **hasCapabilities** (List<String> *capabilities*)
    Test to see if the capabilities array contains a given set of
    capabilities. See the individual Capability classes for acceptable
    capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**

    * capabilities – Array of capabilities to test against

boolean **hasCapabilities** (String... *capabilites*)
    Test to see if the capabilities array contains a given set of
    capabilities. See the individual Capability classes for acceptable
    capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**

    * capabilites – Array of capabilities to test against

:doc:`Launcher <and-launcher>` **getLauncher** ()
    Accessor for highest priority Launcher object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()
    Accessor for highest priority MediaPlayer object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()
    Accessor for highest priority MediaControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()
    Accessor for highest priority PlaylistControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()
    Accessor for highest priority VolumeControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`WebAppLauncher <and-webapplauncher>` **getWebAppLauncher** ()
    Accessor for highest priority WebAppLauncher object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`TVControl <and-tvcontrol>` **getTVControl** ()
    Accessor for highest priority TVControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`ToastControl <and-toastcontrol>` **getToastControl** ()
    Accessor for highest priority ToastControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()
    Accessor for highest priority TextInputControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`MouseControl <and-mousecontrol>` **getMouseControl** ()
    Accessor for highest priority MouseControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`ExternalInputControl <and-externalinputcontrol>` **getExternalInputControl** ()
    Accessor for highest priority ExternalInputControl object This method
    is deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`PowerControl <and-powercontrol>` **getPowerControl** ()
    Accessor for highest priority PowerLauncher object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

:doc:`KeyControl <and-keycontrol>` **getKeyControl** ()
    Accessor for highest priority KeyControl object This method is
    deprecated. Use
    ``ConnectableDevice::getCapability(Class<T> controllerClass)`` method
    instead

void **setIpAddress** (String *ipAddress*)
    Sets the IP address of the ConnectableDevice.

    **Parameters:**

    * ipAddress – IP address of the ConnectableDevice

String **getIpAddress** ()
    Gets the Current IP address of the ConnectableDevice.

void **setFriendlyName** (String *friendlyName*)
    Sets an estimate of the ConnectableDevice's current friendly name.

    **Parameters:**

    * friendlyName – Friendly name of the device

String **getFriendlyName** ()
    Gets an estimate of the ConnectableDevice's current friendly name.

void **setLastKnownIPAddress** (String *lastKnownIPAddress*)
    Sets the last IP address this ConnectableDevice was discovered at.

    **Parameters:**

    * lastKnownIPAddress – Last known IP address of the device & it's services

String **getLastKnownIPAddress** ()
    Gets the last IP address this ConnectableDevice was discovered at.

void **setLastSeenOnWifi** (String *lastSeenOnWifi*)
    Sets the name of the last wireless network this ConnectableDevice was
    discovered on.

    **Parameters:**

    * lastSeenOnWifi – Last Wi-Fi network this device & it's services were discovered on

String **getLastSeenOnWifi** ()
    Gets the name of the last wireless network this ConnectableDevice was
    discovered on.

void **setLastConnected** (long *lastConnected*)
    Sets the last time (in milli seconds from 1970) that this
    ConnectableDevice was connected to.

    **Parameters:**

    * lastConnected – Last connected time

long **getLastConnected** ()
    Gets the last time (in milli seconds from 1970) that this
    ConnectableDevice was connected to.

void **setLastDetection** (long *lastDetection*)
    Sets the last time (in milli seconds from 1970) that this
    ConnectableDevice was detected.

    **Parameters:**

    * lastDetection – Last detected time

long **getLastDetection** ()
    Gets the last time (in milli seconds from 1970) that this
    ConnectableDevice was detected.

void **setModelName** (String *modelName*)
    Sets an estimate of the ConnectableDevice's current model name.

    **Parameters:**

    * modelName – Model name of the ConnectableDevice

String **getModelName** ()
    Gets an estimate of the ConnectableDevice's current model name.

void **setModelNumber** (String *modelNumber*)
    Sets an estimate of the ConnectableDevice's current model number.

    **Parameters:**

    * modelNumber – Model number of the ConnectableDevice

String **getModelNumber** ()
    Gets an estimate of the ConnectableDevice's current model number.

void **setId** (String *id*)
    Sets the universally unique id of this particular ConnectableDevice
    object. This is used internally in the SDK and should not be used.

    **Parameters:**

    * id – New id for the ConnectableDevice

String **getId** ()
    Universally unique id of this particular ConnectableDevice object,
    persists between sessions in ConnectableDeviceStore for connected
    devices

public<T extends CapabilityMethods> T **getCapability** (Class<T> *controllerClass*)
    Get a capability with the highest priority from a device. If device
    doesn't have such capability then returns null.

    **Parameters:**

    * controllerClass – type of capability

    **Returns:** capability implementation

Inherited Methods
-----------------

void **onConnectionRequired** (:doc:`DeviceService <and-deviceservice>` *service*)
    If the DeviceService requires an active connection (websocket,
    pairing, etc) this method will be called.

    **Parameters:**

    * service – DeviceService that requires connection

void **onConnectionSuccess** (:doc:`DeviceService <and-deviceservice>` *service*)
    After the connection has been successfully established, and after
    pairing (if applicable), this method will be called.

    **Parameters:**

    * service – DeviceService that was successfully connected

void **onCapabilitiesUpdated** (:doc:`DeviceService <and-deviceservice>` *service*, List<String> *added*, List<String> *removed*)
    There are situations in which a DeviceService will update the
    capabilities it supports and propagate these changes to the
    DeviceService. Such situations include:

    *  on discovery, DIALService will reach out to detect if certain apps are installed
    *  on discovery, certain DeviceServices need to reach out for version & region information

    For more information on this particular method, see
    ConnectableDeviceDelegate's
    connectableDevice:capabilitiesAdded:removed: method.

    **Parameters:**

    *  service – DeviceService that has experienced a change in capabilities
    *  added – List<String> of capabilities that are new to the DeviceService
    *  removed – List<String> of capabilities that the DeviceService has lost

void **onDisconnect** (:doc:`DeviceService <and-deviceservice>` *service*, Error *error*)
    This method will be called on any disconnection. If error is nil,
    then the connection was clean and likely triggered by the responsible
    DiscoveryProvider or by the user.

    **Parameters:**

    *  service – DeviceService that disconnected
    *  error – Error with a description of any errors causing the disconnect. If this value is nil, then the disconnect was clean/expected.

void **onConnectionFailure** (:doc:`DeviceService <and-deviceservice>` *service*, Error *error*)
    Will be called if the DeviceService fails to establish a connection.

    **Parameters:**

    *  service – DeviceService which has failed to connect
    *  error – Error with a description of the failure

void **onPairingRequired** (:doc:`DeviceService <and-deviceservice>` *service*, :doc:`PairingType <and-pairingtype>` *pairingType*, Object *pairingData*)
    If the DeviceService requires pairing, valuable data will be passed
    to the delegate via this method.

    **Parameters:**

    *  service – DeviceService that requires pairing
    *  pairingType – PairingType that the DeviceService requires
    *  pairingData – Any data that might be required for the pairing process, will usually be nil

void **onPairingSuccess** (:doc:`DeviceService <and-deviceservice>` *service*)

    **Parameters:**

    *  service

void **onPairingFailed** (:doc:`DeviceService <and-deviceservice>` *service*, Error *error*)
    If there is any error in pairing, this method will be called.

    **Parameters:**

    *  service – DeviceService that has failed to complete pairing
    *  error – Error with a description of the failure
