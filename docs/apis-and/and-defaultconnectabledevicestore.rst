DefaultConnectableDeviceStore 
=============================
``com.connectsdk.device.DefaultConnectableDeviceStore``

Default implementation of ConnectableDeviceStore. It stores data in a
file in application data directory.

Properties
----------

long created
    Date (in seconds from 1970) that the ConnectableDeviceStore was
    created.

long updated
    Date (in seconds from 1970) that the ConnectableDeviceStore was last
    updated.

int version
    Current version of the ConnectableDeviceStore, may be necessary for
    migrations

long maxStoreDuration = TimeUnit.DAYS.toSeconds(3)
    Max length of time for a ConnectableDevice to remain in the
    ConnectableDeviceStore without being discovered. Default is 3 days,
    and modifications to this value will trigger a scan for old devices.

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

void **removeAll** ()
    Clears out the ConnectableDeviceStore, removing all records.

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

Inherited Methods
-----------------

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
