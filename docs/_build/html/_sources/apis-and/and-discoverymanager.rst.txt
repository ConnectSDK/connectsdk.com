DiscoveryManager
================
``com.connectsdk.discovery.DiscoveryManager``

Overview
--------

At the heart of Connect SDK is DiscoveryManager, a multi-protocol
service discovery engine with a pluggable architecture. Much of your
initial experience with Connect SDK will be with the DiscoveryManager
class, as it consolidates discovered service information into
ConnectableDevice objects.

In depth
--------

DiscoveryManager supports discovering services of differing protocols by
using DiscoveryProviders. Many services are discoverable over
`SSDP <http://tools.ietf.org/html/draft-cai-ssdp-v1-03>`__ and are
registered to be discovered with the SSDPDiscoveryProvider class.

As services are discovered on the network, the DiscoveryProviders will
notify DiscoveryManager. DiscoveryManager is capable of attributing
multiple services, if applicable, to a single ConnectableDevice
instance. Thus, it is possible to have a mixed-mode ConnectableDevice
object that is theoretically capable of more functionality than a single
service can provide.

DiscoveryManager keeps a running list of all discovered devices and
maintains a filtered list of devices that have satisfied any of your
CapabilityFilters. This filtered list is used by the DevicePicker when
presenting the user with a list of devices.

Only one instance of the DiscoveryManager should be in memory at a time.
To assist with this, DiscoveryManager has static method at
sharedManager.

Example:

.. code-block:: java

    DiscoveryManager.init(getApplicationContext());
    DiscoveryManager discoveryManager = DiscoveryManager.getInstance();
    discoveryManager.addListener(this);
    discoveryManager.start();

Inner Classes
-------------

-  :doc:`PairingLevel <and-pairinglevel>`

Methods
-------

static void **init** (Context *context*)
    Initilizes the Discovery manager with a valid context. This should be
    done as soon as possible and it should use getApplicationContext() as
    the Discovery manager could persist longer than the current Activity.

    .. code-block:: java

        DiscoveryManager.init(getApplicationContext());

    **Parameters:**

    -  context

static void **destroy** ()

static void **init** (Context *context*, :doc:`ConnectableDeviceStore <and-connectabledevicestore>` *connectableDeviceStore*)
    Initilizes the Discovery manager with a valid context. This should be
    done as soon as possible and it should use getApplicationContext() as
    the Discovery manager could persist longer than the current Activity.

    This accepts a ConnectableDeviceStore to use instead of the default
    device store.

    .. code-block:: java

        MyConnectableDeviceStore myDeviceStore = new MyConnectableDeviceStore();
        DiscoveryManager.init(getApplicationContext(), myDeviceStore);

    **Parameters:**

    -  context
    -  connectableDeviceStore

static :doc:`DiscoveryManager <and-discoverymanager>` **getInstance** ()
    Get a shared instance of DiscoveryManager.

void **addListener** (:doc:`DiscoveryManagerListener <and-discoverymanagerlistener>` *listener*)
    Listener which should receive discovery updates. It is not necessary
    to set this listener property unless you are implementing your own
    device picker. Connect SDK provides a default DevicePicker which acts
    as a DiscoveryManagerListener, and should work for most cases.

    If you have provided a capabilityFilters array, the listener will
    only receive update messages for ConnectableDevices which satisfy at
    least one of the CapabilityFilters. If no capabilityFilters array is
    provided, the listener will receive update messages for all
    ConnectableDevice objects that are discovered.

    **Parameters:**

    -  listener – (optional) DiscoveryManagerListener with methods to be called on success or failure

void **removeListener** (:doc:`DiscoveryManagerListener <and-discoverymanagerlistener>` *listener*)
    Removes a previously added listener

    **Parameters:**

    -  listener – (optional) DiscoveryManagerListener with methods to be called on success or failure

void **setCapabilityFilters** (:doc:`CapabilityFilter <and-capabilityfilter>`... *capabilityFilters*)
    **Parameters:**

    -  capabilityFilters

void **setCapabilityFilters** (List<:doc:`CapabilityFilter <and-capabilityfilter>`> *capabilityFilters*)
    **Parameters:**

    -  capabilityFilters

List<:doc:`CapabilityFilter <and-capabilityfilter>`> **getCapabilityFilters** ()
    Returns the list of capability filters.

boolean **deviceIsCompatible** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    **Parameters:**

    -  device

void **start** ()
    Start scanning for devices on the local network.

void **stop** ()
    Stop scanning for devices.

void **setConnectableDeviceStore** (:doc:`ConnectableDeviceStore <and-connectabledevicestore>` *connectableDeviceStore*)
    ConnectableDeviceStore object which loads & stores references to all
    discovered devices. Pairing codes/keys, SSL certificates, recent
    access times, etc are kept in the device store.

    ConnectableDeviceStore is a protocol which may be implemented as
    needed. A default implementation, DefaultConnectableDeviceStore,
    exists for convenience and will be used if no other device store is
    provided.

    In order to satisfy user privacy concerns, you should provide a UI
    element in your app which exposes the ConnectableDeviceStore
    removeAll method.

    To disable the ConnectableDeviceStore capabilities of Connect SDK,
    set this value to nil. This may be done at the time of instantiation
    with ``DiscoveryManager.init(context, null);``.

    **Parameters:**

    -  connectableDeviceStore

:doc:`ConnectableDeviceStore <and-connectabledevicestore>` **getConnectableDeviceStore** ()
    ConnectableDeviceStore object which loads & stores references to all
    discovered devices. Pairing codes/keys, SSL certificates, recent
    access times, etc are kept in the device store.

    ConnectableDeviceStore is a protocol which may be implemented as
    needed. A default implementation, DefaultConnectableDeviceStore,
    exists for convenience and will be used if no other device store is
    provided.

    In order to satisfy user privacy concerns, you should provide a UI
    element in your app which exposes the ConnectableDeviceStore
    removeAll method.

    To disable the ConnectableDeviceStore capabilities of Connect SDK,
    set this value to nil. This may be done at the time of instantiation
    with ``DiscoveryManager.init(context, null);``.

Map<String, :doc:`ConnectableDevice <and-connectabledevice>`> **getAllDevices** ()
    List of all devices discovered by DiscoveryManager. Each
    ConnectableDevice object is keyed against its current IP address.

Map<String, :doc:`ConnectableDevice <and-connectabledevice>`> **getCompatibleDevices** ()
    Filtered list of discovered ConnectableDevices, limited to devices
    that match at least one of the CapabilityFilters in the
    capabilityFilters array. Each ConnectableDevice object is keyed
    against its current IP address.

:doc:`PairingLevel <and-pairinglevel>` **getPairingLevel** ()
    The pairingLevel property determines whether capabilities that
    require pairing (such as entering a PIN) will be available. 

    If pairingLevel is set to ConnectableDevicePairingLevelOn,
    ConnectableDevices that require pairing will prompt the user to pair
    when connecting to the ConnectableDevice.

    If pairingLevel is set to ConnectableDevicePairingLevelOff (the
    default), connecting to the device will avoid requiring pairing if
    possible but some capabilities may not be available.

void **setPairingLevel** (:doc:`PairingLevel <and-pairinglevel>` *pairingLevel*)
    The pairingLevel property determines whether capabilities that
    require pairing (such as entering a PIN) will be available.

    If pairingLevel is set to ConnectableDevicePairingLevelOn,
    ConnectableDevices that require pairing will prompt the user to pair
    when connecting to the ConnectableDevice.

    If pairingLevel is set to ConnectableDevicePairingLevelOff (the
    default), connecting to the device will avoid requiring pairing if
    possible but some capabilities may not be available.

    **Parameters:**

    -  pairingLevel

Inherited Methods
-----------------

void **onDeviceReady** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    A ConnectableDevice sends out a ready message when all of its
    connectable DeviceServices have been connected and are ready to
    receive commands.

    **Parameters:**

    -  device – ConnectableDevice that is ready for commands.

void **onDeviceDisconnected** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    When all of a ConnectableDevice's DeviceServices have become
    disconnected, the disconnected message is sent.

    **Parameters:**

    -  device – ConnectableDevice that has been disconnected.

void **onPairingRequired** (:doc:`ConnectableDevice <and-connectabledevice>` *device*, :doc:`DeviceService <and-deviceservice>` *service*, :doc:`PairingType <and-pairingtype>` *pairingType*)
    DeviceService listener proxy method.

    This method is called when a DeviceService tries to connect and finds
    out that it requires pairing information from the user.

    **Parameters:**

    -  device – ConnectableDevice containing the DeviceService
    -  service – DeviceService that requires pairing
    -  pairingType – DeviceServicePairingType that the DeviceService requires

void **onCapabilityUpdated** (:doc:`ConnectableDevice <and-connectabledevice>` *device*, List<String> *added*, List<String> *removed*)
    When a ConnectableDevice finds & loses DeviceServices, that
    ConnectableDevice will experience a change in its collective
    capabilities list. When such a change occurs, this message will be
    sent with arrays of capabilities that were added & removed.

    This message will allow you to decide when to stop/start interacting
    with a ConnectableDevice, based off of its supported capabilities.

    **Parameters:**

    -  device – ConnectableDevice that has experienced a change in capabilities
    -  added – List<String> of capabilities that are new to the ConnectableDevice
    -  removed – List<String> of capabilities that the ConnectableDevice has lost

void **onConnectionFailed** (:doc:`ConnectableDevice <and-connectabledevice>` *device*, :doc:`ServiceCommandError <and-servicecommanderror>` *error*)
    This method is called when the connection to the ConnectableDevice
    has failed.

    **Parameters:**

    -  device – ConnectableDevice that has failed to connect
    -  error – ServiceCommandError with a description of the failure

void **onServiceAdded** (DiscoveryProvider *provider*, ServiceDescription *serviceDescription*)
    This method is called when the DiscoveryProvider discovers a service
    that matches one of its DeviceService filters. The ServiceDescription
    is created and passed to the listener (which should be the
    DiscoveryManager). The ServiceDescription is used to create a
    DeviceService, which is then attached to a ConnectableDevice object.

    **Parameters:**

    -  provider – DiscoveryProvider that found the service
    -  serviceDescription

void **onServiceRemoved** (DiscoveryProvider *provider*, ServiceDescription *serviceDescription*)
    This method is called when the DiscoveryProvider's internal mechanism
    loses reference to a service that matches one of its DeviceService
    filters.

    **Parameters:**

    -  provider – DiscoveryProvider that lost the service
    -  serviceDescription

void **onServiceDiscoveryFailed** (DiscoveryProvider *provider*, :doc:`ServiceCommandError <and-servicecommanderror>` *error*)
    This method is called on any error/failure within the
    DiscoveryProvider.

    **Parameters:**

    -  provider – DiscoveryProvider that failed
    -  error – ServiceCommandError providing a information about the failure

void **onServiceConfigUpdate** (ServiceConfig *serviceConfig*)
    **Parameters:**

    -  serviceConfig
