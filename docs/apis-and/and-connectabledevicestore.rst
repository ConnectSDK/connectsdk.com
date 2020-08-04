ConnectableDeviceStore com.connectsdk.device.ConnectableDeviceStore
===================================================================

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

   -  avoid tracking too much data (indefinitely storing all discovered
      devices)

periodically remove ConnectableDevices from the ConnectableDeviceStore
if they haven't been used/connected in X amount of time

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

void **removeAll** ()
   Clears out the ConnectableDeviceStore, removing all records.
