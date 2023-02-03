DiscoveryManagerListener
========================
``com.connectsdk.discovery.DiscoveryManagerListener``

Overview
--------

The DiscoveryManagerListener will receive events on the
addition/removal/update of ConnectableDevice objects.

In Depth
--------

It is important to note that, unless you are implementing your own
device picker, this listener is not needed in your code. Connect SDK's
DevicePicker internally acts a separate listener to the DiscoveryManager
and handles all of the same method calls.

Methods
-------

void **onDeviceAdded** (:doc:`DiscoveryManager <and-discoverymanager>` *manager*, :doc:`ConnectableDevice <and-connectabledevice>` *device*)
    This method will be fired upon the first discovery of one of a
    ConnectableDevice's DeviceServices.

    **Parameters:**

    -  manager – DiscoveryManager that found device
    -  device – ConnectableDevice that was found

void **onDeviceUpdated** (:doc:`DiscoveryManager <and-discoverymanager>` *manager*, :doc:`ConnectableDevice <and-connectabledevice>` *device*)
    This method is called when a ConnectableDevice gains or loses a
    DeviceService in discovery.

    **Parameters:**

    -  manager – DiscoveryManager that updated device
    -  device – ConnectableDevice that was updated

void **onDeviceRemoved** (:doc:`DiscoveryManager <and-discoverymanager>` *manager*, :doc:`ConnectableDevice <and-connectabledevice>` *device*)
    This method is called when connections to all of a
    ConnectableDevice's DeviceServices are lost. This will usually happen
    when a device is powered off or loses internet connectivity.

    **Parameters:**

    -  manager – DiscoveryManager that lost device
    -  device – ConnectableDevice that was lost

void **onDiscoveryFailed** (:doc:`DiscoveryManager <and-discoverymanager>` *manager*, :doc:`ServiceCommandError <and-servicecommanderror>` *error*)
    In the event of an error in the discovery phase, this method will be
    called.

    **Parameters:**

    -  manager – DiscoveryManager that experienced the error
    -  error – NSError with a description of the failure
