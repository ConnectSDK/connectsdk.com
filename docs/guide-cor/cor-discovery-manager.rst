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

.. code-block:: javascript

   ConnectSDK.discoveryManager.startDiscovery();

Features
--------

Filtering devices by capability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It will be necessary in many cases to filter out devices that don't
support a desired feature-set. DiscoveryManager provides the
setCapabilityFilters method to provide for this ability.

Here is a simple example that discovers devices that support (video
playback AND any media controls AND volume up/down) OR (image display).

.. code-block:: javascript

   var videoFilter = new ConnectSDK.CapabilityFilter([
       ConnectSDK.Capabilities.MediaPlayer.Play.Video,
       ConnectSDK.Capabilities.MediaControl.Any,
       ConnectSDK.Capabilities.VolumeControl.UpDown
       ]);

   var imageFilter = new ConnectSDK.CapabilityFilter([
       ConnectSDK.Capabilities.MediaPlayer.Display.Image
       ]);

   ConnectSDK.discoveryManager.setCapabilityFilters([videoFilter, imageFilter]);
   app.setupDiscovery();


Pairing level
~~~~~~~~~~~~~

Connect SDK has support for pairing with certain devices. Having pairing
disabled may reduce the number of supported capabilities that a
ConnectableDevice has. Certain devices, although they may support the
features you are filtering for, may not pass your CapabilityFilter if
pairing is disabled.

See the `Supported Features`_ list for information on what devices
require pairing for certain capabilities.

.. _Supported Features: ../fundamentals/supported-feature

For the best user experience, Connect SDK has disabled pairing by
default. Pairing can be enabled very easily, but it must be enabled
before DiscoveryManager is started for the first time.

.. code-block:: javascript

   // Include capabilities that require pairing
   ConnectSDK.discoveryManager.setPairingLevel(ConnectSDK.PairingLevel.ON);

   // Exclude capabilities that require pairing (this is the default)
   ConnectSDK.discoveryManager.setPairingLevel(ConnectSDK.PairingLevel.OFF);

Automatic stop/resume on app state change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If DiscoveryManager is running while your app enters a background state,
it will resume immediately upon returning to a foreground state. This is
to prevent battery drain on the user's device.

.. seealso::

  * :doc:`DiscoveryManager <../apis-cor/cor-discovery-manager>`
  * :doc:`CapabilityFilter <../apis-cor/cor-capabilityfilter>`
