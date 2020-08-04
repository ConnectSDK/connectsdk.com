DefaultConnectableDeviceStore com.connectsdk.device.DefaultConnectableDeviceStore
=================================================================================

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

void **addDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Add a ConnectableDevice to the ConnectableDeviceStore. If the
   ConnectableDevice is already stored, it's record will be updated.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  device –

      ConnectableDevice to add to the ConnectableDeviceStore

void **removeDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Removes a ConnectableDevice's record from the ConnectableDeviceStore.

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  device –

      ConnectableDevice to remove from the ConnectableDeviceStore

void **updateDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Updates a ConnectableDevice's record in the ConnectableDeviceStore.

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  device –

      ConnectableDevice to update in the ConnectableDeviceStore

void **removeAll** ()
   Clears out the ConnectableDeviceStore, removing all records.

JSONObject **getStoredDevices** ()
   A JSONObject of all ConnectableDevices in the ConnectableDeviceStore.
   To gt a strongly-typed ConnectableDevice object, use the
   ``getDevice(String);`` method.

`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ **getDevice** (String *uuid*)
   Gets a ConnectableDevice object for a provided id. The id may be for
   the ConnectableDevice object or any of the DeviceServices.

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  uuid –

      Unique ID for a ConnectableDevice or any of its DeviceService
      objects

   .. rubric:: Returns:
      :name: returns
      :class: method-detail-label

   ConnectableDevice object if a matching uuit was found, otherwise will
   return null

ServiceConfig **getServiceConfig** (ServiceDescription *serviceDescription*)
   Gets a ServcieConfig object for a provided UUID. This is used by
   DiscoveryManager to retain crucial service information between
   sessions (pairing code, etc).

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  serviceDescription –

      Description for the service

   .. rubric:: Returns:
      :name: returns-1
      :class: method-detail-label

   ServiceConfig object if matching description was found, otherwise
   will return null

Inherited Methods
-----------------

void **addDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Add a ConnectableDevice to the ConnectableDeviceStore. If the
   ConnectableDevice is already stored, it's record will be updated.

   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  device –

      ConnectableDevice to add to the ConnectableDeviceStore

void **removeDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Removes a ConnectableDevice's record from the ConnectableDeviceStore.

   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  device –

      ConnectableDevice to remove from the ConnectableDeviceStore

void **updateDevice** (`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ *device*)
   Updates a ConnectableDevice's record in the ConnectableDeviceStore.

   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  device –

      ConnectableDevice to update in the ConnectableDeviceStore

JSONObject **getStoredDevices** ()
   A JSONObject of all ConnectableDevices in the ConnectableDeviceStore.
   To gt a strongly-typed ConnectableDevice object, use the
   ``getDevice(String);`` method.

`ConnectableDevice </apis/1-6-0/android/ConnectableDevice>`__ **getDevice** (String *uuid*)
   Gets a ConnectableDevice object for a provided id. The id may be for
   the ConnectableDevice object or any of the DeviceServices.

   .. rubric:: Parameters:
      :name: parameters-8
      :class: method-detail-label

   -  uuid –

      Unique ID for a ConnectableDevice or any of its DeviceService
      objects

   .. rubric:: Returns:
      :name: returns-2
      :class: method-detail-label

   ConnectableDevice object if a matching uuit was found, otherwise will
   return null

ServiceConfig **getServiceConfig** (ServiceDescription *serviceDescription*)
   Gets a ServcieConfig object for a provided UUID. This is used by
   DiscoveryManager to retain crucial service information between
   sessions (pairing code, etc).

   .. rubric:: Parameters:
      :name: parameters-9
      :class: method-detail-label

   -  serviceDescription –

      Description for the service

   .. rubric:: Returns:
      :name: returns-3
      :class: method-detail-label

   ServiceConfig object if matching description was found, otherwise
   will return null

void **removeAll** ()
   Clears out the ConnectableDeviceStore, removing all records.
