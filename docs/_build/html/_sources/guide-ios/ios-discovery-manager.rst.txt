Discovery Manager
=================

At the heart of Connect SDK is DiscoveryManager, a multi-protocol
service discovery engine with a pluggable architecture. Much of your
initial experience with Connect SDK will be with the DiscoveryManager
class, as it consolidates discovered service information into
ConnectableDevice objects.

DiscoveryManager supports discovering services of differing protocols by
using DiscoveryProviders. Many services are discoverable over SSDP and
are registered to be discovered with the SSDPDiscoveryProvider class.

As services are discovered on the network, the DiscoveryProviders will
notify DiscoveryManager. DiscoveryManager is capable of attributing
multiple services, if applicable, to a single ConnectableDevice
instance. Thus, it is possible to have a mixed-mode ConnectableDevice
object that is theoretically capable of more functionality than a single
service can provide.

DiscoveryManager keeps a running list of all discovered devices and
maintains a filtered list of devices that have satisfied any of your
CapabilityFilters. This filtered list is used by the DevicePicker when
presenting the user with a list of devices.

Connect SDK device discovery can be started in one line.

.. code-block:: obj-c

   [[DiscoveryManager sharedManager] startDiscovery];

Features
--------

Filtering devices by capability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It will be necessary in many cases to filter out devices that don't
support a desired feature-set. DiscoveryManager provides the
setCapabilityFilters method to provide for this ability.

Here is a simple example that discovers devices that support (video
playback AND any media controls AND volume up/down) OR (image display).

.. code-block:: obj-c

   NSArray *videoCapabilities = @[
       kMediaPlayerDisplayVideo,
       kMediaControlAny,
       kVolumeControlVolumeUpDown
   ];

   NSArray *imageCapabilities = @[
       kMediaPlayerDisplayImage
   ];

   CapabilityFilter *videoFilter = [CapabilityFilter filterWithCapabilities:videoCapabilities];
   CapabilityFilter *imageFilter = [CapabilityFilter filterWithCapabilities:imageCapabilities];

   [[DiscoveryManager sharedManager] setCapabilityFilters:@[videoFilter, imageFilter]];

DeviceService registration
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Connect SDK is configured to discover all the services that
it supports (webOS, Netcast, Chromecast, AirPlay, DIAL, & Roku). It is
possible to support only a subset of these services by manually
registering those services before starting DiscoveryManager for the
first time.

.. code-block:: obj-c

   [[DiscoveryManager sharedManager] registerDeviceService:[AirPlayService class] withDiscovery:[ZeroconfDiscoveryProvider class]];
   [[DiscoveryManager sharedManager] registerDeviceService:[CastService class] withDiscovery:[CastDiscoveryProvider class]];
   [[DiscoveryManager sharedManager] registerDeviceService:[DIALService class] withDiscovery:[SSDPDiscoveryProvider class]];
   [[DiscoveryManager sharedManager] registerDeviceService:[RokuService class] withDiscovery:[SSDPDiscoveryProvider  class]];
   [[DiscoveryManager sharedManager] registerDeviceService:[DLNAService class] withDiscovery:[SSDPDiscoveryProvider class]]; // LG TV devices only, includes NetcastTVService
   [[DiscoveryManager sharedManager] registerDeviceService:[WebOSTVService class] withDiscovery:[SSDPDiscoveryProvider class]];

Automatic stop/resume on app state change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If DiscoveryManager is running while your app enters a background state,
it will resume immediately upon returning to a foreground state. This is
to prevent battery drain on the user's device.

Pairing level
~~~~~~~~~~~~~

Connect SDK has support for pairing with certain devices. To have
pairing disabled may reduce the number of supported capabilities that a
ConnectableDevice has. Certain devices, although they may support the
features you are filtering for, may not pass your CapabilityFilter if
pairing is disabled.

See the :doc:`Supported Features <../fundamentals/supported-feature>` list for
information on what devices require pairing for certain capabilities.

For the best user experience, Connect SDK has disabled pairing by
default. Pairing can be enabled very easily, but it must be enabled
before DiscoveryManager is started for the first time.

.. code-block:: obj-c

   [DiscoveryManager sharedManager].pairingLevel = DeviceServicePairingLevelOn;

Device store
~~~~~~~~~~~~

When connecting with a device certain information is retained about that
connection. This information is helpful for app relaunches, pairing,
remembering commonly-used devices, and more. Connect SDK provides a
ConnectableDeviceStore protocol to allow you to store ConnectableDevice
information in a manner that suits your use case.

A default implementation, DefaultConnectableDeviceStore, will be used by
DiscoveryManager if no other ConnectableDeviceStore is provided to
DiscoveryManager when startDiscovery is called.

.. seealso::

  * :doc:`DiscoveryManager <../apis-ios/ios-discoverymanager>`
  * :doc:`CapabilityFilter <../apis-ios/ios-capabilityfilter>`
  * :doc:`PairingLevel <../apis-ios/ios-deviceservicepairinglevel>`
  * :doc:`ConnectableDeviceStore <../apis-ios/ios-connectabledevicestore>`
  * :doc:`DefaultConnectableDeviceStore <../apis-ios/ios-defaultconnectabledevicestore>`
