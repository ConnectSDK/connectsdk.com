Discover & Connect to Device
============================

Initial setup
-------------

Your view controller should implement delegate/listener methods for
Connect SDK's DevicePicker and ConnectableDevice classes. These methods
will give you the ability to respond to device selection, ready,
disconnect, and error states.

.. code-block:: objective-c

   @interface ViewController () <DevicePickerDelegate, ConnectableDeviceDelegate>
   @end

It is helpful to retain local references to both the DiscoveryManager
and the ConnectableDevice objects. In most use cases, these two classes
will serve to provide most of the functionality required.

.. code-block:: objective-c

   @implementation ViewController
   {
       DiscoveryManager *_discoveryManager;
       ConnectableDevice *_device;
   }

As soon as your app loads, you should instantiate the DiscoveryManager
singleton and start discovery. As different devices can take a wide
range of time to be discovered, it is recommended that discovery start
as soon as possible after app launch.

.. code-block:: objective-c

   - (void)viewDidLoad
   {
       [super viewDidLoad];

       // This step could even happen in your app's delegate
       _discoveryManager = [DiscoveryManager sharedManager];
       [_discoveryManager startDiscovery];
   }

Discovery & device selection
----------------------------

In many cases, your user will want to select one device from a list of
many. You should present the DevicePicker to the user to receive their
selection. The DevicePicker includes a dynamic listing of all devices
that have been discovered on the network.

Passing the "sender" property of an IBAction will allow the SDK to
present a popover view from a UIView if the user is on an iPad.

.. code-block:: objective-c

   - (IBAction)hShareImage:(id)sender
   {
       _discoveryManager.devicePicker.delegate = self;
       [_discoveryManager.devicePicker showPicker:sender];
   }

Once the user has selected a device, you should immediately register for
events from that device and then call the connect method.

.. code-block:: objective-c

   - (void)devicePicker:(DevicePicker *)picker didSelectDevice:(ConnectableDevice *)device
   {
       _device = device;
       _device.delegate = self;
       [_device connect];
   }

Capability Filtering
~~~~~~~~~~~~~~~~~~~~

If your app is making use of certain device capabilities (media
playback/controls, web app launching, etc), it is strongly recommended
that you create filters with this information for DiscoveryManager.

Devices that are discovered & shown in the picker will be guaranteed to
have the set of capabilities that you have provided. This will prevent
your users from selecting a device that has not yet acquired all of its
protocols.

.. code-block:: objective-c

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

Check out the article on
:doc:`capabilities <ios-checking-capabilities>` for more depth
on this topic.
