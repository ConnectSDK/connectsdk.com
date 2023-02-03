DefaultConnectableDeviceStore
=============================

DefaultConnectableDeviceStore is an implementation of
ConnectableDeviceStore provided by Connect SDK for your convenience.
This class will be used by DiscoveryManager as the default
ConnectableDeviceStore if no other ConnectableDeviceStore implementation
is provided before calling startDiscovery.

Privacy Considerations
----------------------

As outlined in ConnectableDeviceStore, this class takes the following
steps to ensure users' privacy.

* Only ConnectableDevices that have been connected to will be permanently stored
* On load & store, ConnectableDevices that have not been discovered within the maxStoreDuration will be removed from the ConnectableDeviceStore

File Format
-----------

DefaultConnectableDeviceStore stores data in a JSON file named ``Connect_SDK_Device_Store.json`` in the documents directory.

.. code-block:: json
   :force:

   {
       // necessary for migrations, if needed
       version: 1,
       created: 1395892958.220422,
       updated: 1395892958.220422,
       devices: {
           "12345678-5137-1358-1544-123456789012" : { // each ConnectableDevice is keyed against its id
               "id": "12345678-5137-1358-1544-123456789012",
               "friendlyName": "My TV",
               "lastKnownIPAddress": "192.168.1.107",
               "lastSeenOnWifi": "My WiFi Network",
               "lastConnected": 1395892958.220422,
               "lastDetection": 1395892958.220422,
               "services": {
                   "66be8e5d-51be-b18f-f733-6c4dc8c97aca": { // each DeviceService discovered is keyed against its UUID
                       {
                           "class": "WebOSTVService", // DeviceService subclass name
                           "config": {
                               "class": "WebOSTVServiceConfig", // ServiceConfig subclass name
                               "UUID": "66be8e5d-51be-b18f-f733-6c4dc8c97aca",
                               "connected": false,
                               "wasConnected": false,
                               "lastDetection": 1395892958.220422,

                               // should be appropriate to the platform (in iOS this is an array)
                               "SSLCertificates": ...,
                               "clientKey": "..."
                           },
                           "description": {
                               "serviceId": "webOS TV",
                               "port": 3001,
                               "UUID": "66be8e5d-51be-b18f-f733-6c4dc8c97aca",
                               "type": "urn:lge-com:service:webos-second-screen:1",
                               "version": "4.1.0",
                               "friendlyName": "My TV",
                               "manufacturer": "LG Electronics",
                               "modelName": "LG Smart TV",
                               "modelDescription": "",
                               "modelNumber": "",
                               "commandURL": "http://192.168.1.107:1914/"
                           }
                       }
                   }
               }
           },
           ...
       }
   }

Properties
----------

double maxStoreDuration
   Max length of time for a ConnectableDevice to remain in the
   ConnectableDeviceStore without being discovered. Default is 3 days,
   and modifications to this value will trigger a scan for old devices.
   ConnectableDevices that have been connected to will never be removed
   from the device store unless ``remove:`` or ``removeAll`` are called.

double created
   Date (in seconds from 1970) that the ConnectableDeviceStore was
   created.

double updated
   Date (in seconds from 1970) that the ConnectableDeviceStore was last
   updated.

int version
   Current version of the ConnectableDeviceStore, may be necessary for
   migrations
