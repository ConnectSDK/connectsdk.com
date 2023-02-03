ConnectableDeviceDelegate
=========================

ConnectableDeviceDelegate allows for a class to receive messages about
ConnectableDevice connection, disconnect, and update events.

It also serves as a delegate proxy for message handling when connecting
and pairing with each of a ConnectableDevice's DeviceServices. Each of
the DeviceService proxy methods are optional and would only be useful in
a few use cases.

* providing your own UI for the pairing process.
* interacting directly and exclusively with a single type of
   DeviceService

Methods
-------

\- (void) **connectableDeviceReady**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   A ConnectableDevice sends out a ready message when all of its
   connectable DeviceServices have been connected and are ready to
   receive commands.

   **Parameters:**

   * device – ConnectableDevice that is ready for commands.

\- (void) **connectableDeviceDisconnected**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **withError**:(NSError \*)\ *error*
   When all of a ConnectableDevice's DeviceServices have become
   disconnected, the disconnected message is sent.

   **Parameters:**

   * device – ConnectableDevice that has been disconnected.
   * **withError**: error

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **capabilitiesAdded**:(NSArray \*)\ *added* **removed**:(NSArray \*)\ *removed*
   When a ConnectableDevice finds & loses DeviceServices, that
   ConnectableDevice will experience a change in its collective
   capabilities list. When such a change occurs, this message will be
   sent with arrays of capabilities that were added & removed.

   This message will allow you to decide when to stop/start interacting
   with a ConnectableDevice, based off of its supported capabilities.

   **Parameters:**

   * device – ConnectableDevice that has experienced a change in capabilities
   * **capabilitiesAdded**: added – NSArray of capabilities that are new to the ConnectableDevice
   * **removed**: removed – NSArray of capabilities that the ConnectableDevice has lost

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **connectionFailedWithError**:(NSError \*)\ *error*
   This method is called when the connection to the ConnectableDevice
   has failed.

   **Parameters:**

   * device – ConnectableDevice that has failed to connect
   * **connectionFailedWithError**: error – NSError with a description of the failure

\- (void) **connectableDeviceConnectionRequired**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **forService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   DeviceService delegate proxy method.

   This method is called when a DeviceService requires an active
   connection. This will be the case for DeviceServices that send
   messages over websockets (webOS, etc) and DeviceServices that require
   pairing to send messages (Netcast, etc).

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **forService**: service – DeviceService which requires a connection

\- (void) **connectableDeviceConnectionSuccess**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **forService**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   DeviceService delegate proxy method.

   This method is called when a DeviceService has successfully connected.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **forService**: service – DeviceService which has connected

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **disconnectedWithError**:(NSError \*)\ *error*
   DeviceService delegate proxy method.

   This method is called when a DeviceService becomes disconnected.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **service**: service – DeviceService which has disconnected
   * **disconnectedWithError**: error – NSError with a description of any errors causing the disconnect. If this value is nil, then the disconnect was clean/expected.

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **didFailConnectWithError**:(NSError \*)\ *error*
   DeviceService delegate proxy method.

   This method is called when a DeviceService fails to connect.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **service**: service – DeviceService which has failed to connect
   * **didFailConnectWithError**: error – NSError with a description of the failure

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **pairingRequiredOfType**:(int)\ *pairingType* **withData**:(id)\ *pairingData*
   DeviceService delegate proxy method.

   This method is called when a DeviceService tries to connect and finds
   out that it requires pairing information from the user.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **service**: service – DeviceService that requires pairing
   * **pairingRequiredOfType**: pairingType – DeviceServicePairingType that the DeviceService requires
   * **withData**: pairingData – Any data that might be required for the pairing process, will usually be nil

\- (void) **connectableDevicePairingSuccess**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   DeviceService delegate proxy method.

   This method is called when a DeviceService completes the pairing process.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **service**: service – DeviceService that has successfully completed pairing

\- (void) **connectableDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service* **pairingFailedWithError**:(NSError \*)\ *error*
   DeviceService delegate proxy method.

   This method is called when a DeviceService fails to complete the
   pairing process.

   **Parameters:**

   * device – ConnectableDevice containing the DeviceService
   * **service**: service – DeviceService that has failed to complete pairing
   * **pairingFailedWithError**: error – NSError with a description of the failure
