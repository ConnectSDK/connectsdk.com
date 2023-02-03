DiscoveryManager
================

ConnectSDK.discoveryManager is the main entry point into ConnectSDK. It
allows finding devices on the local network and displaying a picker to
select and connect to a device. DiscoveryManager should always be
accessed through its singleton instance, ConnectSDK.discoveryManager.

DiscoveryManager emits the following events while active:

-  startdiscovery
-  stopdiscovery
-  devicelistchanged
-  devicefound (device)
-  devicelost (device)
-  deviceupdated (device)

Methods
-------

discoveryManager.\ **startDiscovery** ([*config*])
   Start searching for devices. DiscoveryManager will start emitting
   events as the device list changes, and populates the device list used
   by pickDevice().

   **Parameters:**

   -  config (Object) [optional] – Dictionary of settings to configure before starting discovery.
      Supported keys are "pairingLevel" and "capabilityFilters". See
      setPairingLevel and setCapabilityFilter for more details.

discoveryManager.\ **stopDiscovery** ()
   Stop searching for devices.

discoveryManager.\ **setPairingLevel** (*pairingLevel*)
   Set pairing level. If set to ConnectSDK.PairingLevel.OFF, the SDK
   will request device capabilities that do not require entering a
   pairing code/confirmation.

   **Parameters:**

   -  pairingLevel (string) – Valid values are the constants ConnectSDK.PairingLevel.ON and
      ConnectSDk.PairingLevel.OFF

discoveryManager.\ **setAirPlayServiceMode** ()
   Set mode for AirPlay support. If set to
   ConnectSDK.AirPlayServiceMode.WebApp, a web app will will be mirrored
   to the TV. If set to ConnectSDK.AirPlayServiceMode.Media, only media
   APIs will be available. On Android, media mode is the only option.

   NOTE: This setting must be configured before calling
   startDiscovery(), or passed in the options parameter to
   startDiscovery(). The mode should not be changed once configured.

discoveryManager.\ **setCapabilityFilters** (*filters*)
   Set capability filters. DiscoveryManager will only show devices that
   match at least one of the CapabilityFilter instances.

   Example:

   .. code-block:: javascript

      // Show devices that support playing videos and pausing OR support launching YouTube with a video id
      ConnectSDK.discoveryManager.setCapabilityFilters([
          new ConnectSDK.CapabilityFilter([ConnectSDK.Capabilities.MediaPlayer.Play.Video, ConnectSDK.Capabilities.MediaControl.Pause])
          new ConnectSDK.CapabilityFilter([ConnectSDK.Capabilities.Launcher.YouTube.Params])
      ])

   **Parameters:**

   -  filters (CapabilityFilter[]) – array of CapabilityFilter objects

discoveryManager.\ **pickDevice** ([*options*])
   Show device picker popup. To get notified when the user has selected
   a device, add a success/error listener to the DevicePicker returned
   when calling this method.

   **Parameters:**

   -  options (Object) [optional] – All keys are optional

      .. code-block:: javascript

         - pairingType (string): PairingType to use

   **Returns:** :doc:`DevicePicker <cor-devicepicker>`

discoveryManager.\ **getDeviceList** ()
   Get a list of discovered devices available on the network.

   **Returns:** :doc:`ConnectableDevice <cor-connectabledevice>`\ []

Mixin Methods - SimpleEventEmitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

discoveryManager.\ **addListener** (*event*, *callback*, [*context*])
   Add event listener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

discoveryManager.\ **removeListener** (*event*, [*callback*], [*context*])
   Remove event listener with the specified callback and context. If
   callback is null or undefined, all callbacks for this event will be
   removed.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) [optional] – function originally passed to addListener

   -  context (object) [optional] – context object originally passed to addListener

   **Returns:** object – reference to the same object to allow chaining

discoveryManager.\ **on** (*event*, *callback*, [*context*])
   Alias for addListener.

   **Parameters:**

   -  event (string) – name of event

   -  callback (function) – function to call when event is fired

   -  context (object) [optional] – object to bind to "this" value when calling function

   **Returns:** object – reference to the same object to allow chaining

discoveryManager.\ **off** (*event*, [*callback*], [*context*])
   Alias for removeListener.

   **Parameters:**

   -  event (string) – event name

   -  callback (function) [optional] – function originally passed to on

   -  context (object) [optional] – context object originally passed to on

   **Returns:** object – reference to the same object to allow chaining
