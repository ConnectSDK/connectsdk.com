DiscoveryManagerDelegate
========================

Overview
--------

The DiscoveryManagerDelegate will receive events on the addition/removal/update of ConnectableDevice objects.

In Depth
--------

It is important to note that, unless you are implementing your own device picker, this delegate is not needed in your code. Connect SDK's
DevicePicker internally acts a separate delegate to the DiscoveryManager and handles all of the same method calls.

Methods
-------

\- (void) **discoveryManager**:(:doc:`DiscoveryManager <ios-discoverymanager>` \*)\ *manager* **didFindDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   This method will be fired upon the first discovery of one of a
   ConnectableDevice's DeviceServices.

   **Parameters:**

   * manager – DiscoveryManager that found device
   * **didFindDevice**: device – ConnectableDevice that was found

\- (void) **discoveryManager**:(:doc:`DiscoveryManager <ios-discoverymanager>` \*)\ *manager* **didLoseDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   This method is called when connections to all of a ConnectableDevice's DeviceServices are lost. This will usually happen when a device is powered off or loses internet connectivity.

   **Parameters:**

   * manager – DiscoveryManager that lost device
   * **didLoseDevice**: device – ConnectableDevice that was lost

\- (void) **discoveryManager**:(:doc:`DiscoveryManager <ios-discoverymanager>` \*)\ *manager* **didUpdateDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   This method is called when a ConnectableDevice gains or loses a DeviceService in discovery.

   **Parameters:**

   * manager – DiscoveryManager that updated device
   * **didUpdateDevice**: device – ConnectableDevice that was updated

\- (void) **discoveryManager**:(:doc:`DiscoveryManager <ios-discoverymanager>` \*)\ *manager* **didFailWithError**:(NSError \*)\ *error*
   In the event of an error in the discovery phase, this method will be called.

   **Parameters:**

   * manager – DiscoveryManager that experienced the error
   * **didFailWithError**: error – NSError with a description of the failure
