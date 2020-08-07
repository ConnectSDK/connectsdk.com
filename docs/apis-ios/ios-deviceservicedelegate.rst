DeviceServiceDelegate
=====================

DeviceServiceDelegate allows your app to respond to each step of the
connection and pairing processes, if needed. By default, a
DeviceService's ConnectableDevice is set as the delegate. Changing a
DeviceService's delegate will break the normal operation of Connect SDK
and is discouraged. ConnectableDeviceDelegate provides proxy methods for
all of the methods listed here.

Methods
-------

\- (void) **deviceServiceConnectionRequired**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   If the DeviceService requires an active connection (websocket,
   pairing, etc) this method will be called.

   **Parameters:**

   * service – DeviceService that requires connection

\- (void) **deviceServiceConnectionSuccess**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   After the connection has been successfully established, and after
   pairing (if applicable), this method will be called.

   **Parameters:**

   * service – DeviceService that was successfully connected

\- (void) **deviceService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **capabilitiesAdded**:(NSArray \*)\ *added* **removed**:(NSArray \*)\ *removed*
   There are situations in which a DeviceService will update the
   capabilities it supports and propagate these changes to the
   DeviceService. Such situations include:

   * on discovery, DIALService will reach out to detect if certain apps are installed
   * on discovery, certain DeviceServices need to reach out for & region information

   For more information on this particular method, see ConnectableDeviceDelegate's connectableDevice:capabilitiesAdded:removed: method.

   **Parameters:**

   * service – DeviceService that has experienced a change in capabilities
   * **capabilitiesAdded**: added – NSArray of capabilities that are new to the DeviceService
   * **removed**: removed – NSArray of capabilities that the DeviceService has lost

\- (void) **deviceService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **disconnectedWithError**:(NSError \*)\ *error*
   This method will be called on any disconnection. If error is nil,
   then the connection was clean and likely triggered by the responsible
   DiscoveryProvider or by the user.

   **Parameters:**

   * service – DeviceService that disconnected

   * **disconnectedWithError**: error – NSError with a description of any errors causing the disconnect. If this value is nil, then the disconnect was clean/expected.

\- (void) **deviceService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **didFailConnectWithError**:(NSError \*)\ *error*
   Will be called if the DeviceService fails to establish a connection.

   **Parameters:**

   * service – DeviceService which has failed to connect
   * **didFailConnectWithError**: error – NSError with a description of the failure

\- (void) **deviceService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **pairingRequiredOfType**:(:doc:`DeviceServicePairingType <ios-deviceservicepairingtype>`)\ *pairingType* **withData**:(id)\ *pairingData*
   If the DeviceService requires pairing, valuable data will be passed
   to the delegate via this method.

   **Parameters:**

   * service – DeviceService that requires pairing
   * **pairingRequiredOfType**: pairingType – DeviceServicePairingType that the DeviceService requires
   * **withData**: pairingData – Any object/data that might be required for the pairing process, will usually be nil

\- (void) **deviceServicePairingSuccess**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   **Parameters:**

   * service

\- (void) **deviceService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **pairingFailedWithError**:(NSError \*)\ *error*
   If there is any error in pairing, this method will be called.

   **Parameters:**

   * service – DeviceService that has failed to complete pairing
   * **pairingFailedWithError**: error – NSError with a description of the failure
