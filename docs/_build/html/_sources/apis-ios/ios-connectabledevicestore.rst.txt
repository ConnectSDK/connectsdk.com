ConnectableDeviceStore
======================

ConnectableDeviceStore is a protocol which can be implemented to save
key information about ConnectableDevices that have been connected to.
Any class which implements this protocol can be used as
DiscoveryManager's deviceStore.

A default implementation, DefaultConnectableDeviceStore, will be used by
DiscoveryManager if no other ConnectableDeviceStore is provided to
DiscoveryManager when startDiscovery is called.

Privacy Considerations
----------------------

If you chose to implement ConnectableDeviceStore, it is important to
keep your users' privacy in mind.

* There should be UI elements in your app to

   * completely disable ConnectableDeviceStore
   * purge all data from ConnectableDeviceStore (removeAll)

* Your ConnectableDeviceStore implementation should

   * avoid tracking too much data (indefinitely storing all discovered devices)
   * periodically remove ConnectableDevices from the ConnectableDeviceStore if they haven't been used/connected in X amount of time

Properties
----------

NSDictionary \* storedDevices
   A dictionary containing information about all ConnectableDevices in
   the ConnectableDeviceStore. To get a strongly-typed ConnectableDevice
   object, use the ``getDeviceForUUID:`` method.

Methods
-------

\- (void) **addDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   Add a ConnectableDevice to the ConnectableDeviceStore. If the
   ConnectableDevice is already stored, it's record will be updated.

   **Parameters:**

   * device – ConnectableDevice to add to the ConnectableDeviceStore

\- (void) **updateDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   Updates a ConnectableDevice's record in the ConnectableDeviceStore.
   If the ConnectableDevice is not in the store, this call will be
   ignored.

   **Parameters:**

   * device – ConnectableDevice to update in the ConnectableDeviceStore

\- (void) **removeDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   Removes a ConnectableDevice's record from the ConnectableDeviceStore.

   **Parameters:**

   * device – ConnectableDevice to remove from the ConnectableDeviceStore

\- (:doc:`ConnectableDevice <ios-connectabledevice>` \*) **deviceForId**:(NSString \*)\ *id*
   Gets a ConnectableDevice object for a provided id. The id may be for
   the ConnectableDevice object or any of the device's DeviceServices.

   **Parameters:**

   * id – Unique ID for a ConnectableDevice or any of its DeviceService objects

   **Returns:** ConnectableDevice object if a matching id was found, otherwise will return nil

\- (ServiceConfig \*) **serviceConfigForUUID**:(NSString \*)\ *UUID*
   Gets a ServiceConfig object for a provided UUID. This is used by
   DiscoveryManager to retain crucial service information between
   sessions (pairing code, etc).

   **Parameters:**

   * UUID – Unique ID for the service
   
   **Returns:** ServiceConfig object if a matching UUID was found, otherwise will return nil

\- (void) **removeAll**
   Clears out the ConnectableDeviceStore, removing all records.
