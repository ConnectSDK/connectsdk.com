ConnectableDeviceStore
======================
``com.connectsdk.device.ConnectableDeviceStore``

ConnectableDeviceStore is a interface which can be implemented to save
key information about ConnectableDevices that have been connected to.
Any class which implements this interface can be used as
DiscoveryManager's deviceStore.

A default implementation, DefaultConnectableDeviceStore, will be used by
DiscoveryManager if no other ConnectableDeviceStore is provided to
DiscoveryManager when startDiscovery is called.

Privacy Considerations
----------------------

If you chose to implement ConnectableDeviceStore, it is important to
keep your users' privacy in mind.

-  There should be UI elements in your app to

    -  completely disable ConnectableDeviceStore
    -  purge all data from ConnectableDeviceStore (removeAll)

-  Your ConnectableDeviceStore implementation should

    -  avoid tracking too much data (indefinitely storing all discovered devices)

periodically remove ConnectableDevices from the ConnectableDeviceStore
if they haven't been used/connected in X amount of time

Methods
-------

void **addDevice** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    Add a ConnectableDevice to the ConnectableDeviceStore. If the
    ConnectableDevice is already stored, it's record will be updated.

    **Parameters:**

    -  device – ConnectableDevice to add to the ConnectableDeviceStore

void **removeDevice** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    Removes a ConnectableDevice's record from the ConnectableDeviceStore.

    **Parameters:**

    -  device – ConnectableDevice to remove from the ConnectableDeviceStore

void **updateDevice** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    Updates a ConnectableDevice's record in the ConnectableDeviceStore.

    **Parameters:**

    -  device – ConnectableDevice to update in the ConnectableDeviceStore

JSONObject **getStoredDevices** ()
    A JSONObject of all ConnectableDevices in the ConnectableDeviceStore.
    To gt a strongly-typed ConnectableDevice object, use the
    ``getDevice(String);`` method.

:doc:`ConnectableDevice <and-connectabledevice>` **getDevice** (String *uuid*)
    Gets a ConnectableDevice object for a provided id. The id may be for
    the ConnectableDevice object or any of the DeviceServices.

    **Parameters:**

    -  uuid – Unique ID for a ConnectableDevice or any of its DeviceService objects

    **Returns:** ConnectableDevice object if a matching uuit was found, otherwise will return null

ServiceConfig **getServiceConfig** (ServiceDescription *serviceDescription*)
    Gets a ServcieConfig object for a provided UUID. This is used by
    DiscoveryManager to retain crucial service information between
    sessions (pairing code, etc).

    **Parameters:**

    -  serviceDescription – Description for the service

    **Returns:** ServiceConfig object if matching description was found, otherwise will return null

void **removeAll** ()
    Clears out the ConnectableDeviceStore, removing all records.
