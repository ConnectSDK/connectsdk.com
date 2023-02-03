ConnectableDeviceListener 
=========================
``com.connectsdk.device.ConnectableDeviceListener``

ConnectableDeviceListener allows for a class to receive messages about
ConnectableDevice connection, disconnect, and update events.

It also serves as a proxy for message handling when connecting and
pairing with each of a ConnectableDevice's DeviceServices. Each of the
DeviceService proxy methods are optional and would only be useful in a
few use cases.

-  providing your own UI for the pairing process.

-  interacting directly and exclusively with a single type of DeviceService

Methods
-------

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
