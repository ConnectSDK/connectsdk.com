CapabilityFilter
================

CapabilityFilter is an object that wraps an NSArray of required
capabilities. This CapabilityFilter is used for determining which
devices will appear in DiscoveryManager's compatibleDevices array. The
contents of a CapabilityFilter's array must be any of the string
constants defined in the Capability header files.

CapabilityFilter values
-----------------------

Here are some examples of values for the Capability constants.

* kMediaPlayerPlayVideo = "MediaPlayer.Display.Video"
* kMediaPlayerDisplayImage = "MediaPlayer.Display.Image"
* kVolumeControlSubscribe = "VolumeControl.Subscribe"
* kMediaControlAny = "Media.Control.Any"

All Capability header files also define a constant array of all
capabilities defined in that header (ex. kVolumeControlCapabilities).

AND/OR Filtering
----------------

CapabilityFilter is an AND filter. A ConnectableDevice would need to
satisfy all conditions of a CapabilityFilter to pass.

[DiscoveryManager capabilityFilters] is an OR filter. a
ConnectableDevice only needs to satisfy one condition (CapabilityFilter)
to pass.

Examples
--------

Filter for all devices that support video playback AND any media
controls AND volume up/down.

.. code-block:: objc

   NSArray *capabilities = @[
       kMediaPlayerPlayVideo,
       kMediaControlAny,
       kVolumeControlVolumeUpDown
   ];

   CapabilityFilter *filter =
       [CapabilityFilter filterWithCapabilities:capabilities];

   [[DiscoveryManager sharedManager] setCapabilityFilters:@[filter]];

Filter for all devices that support (video playback AND any media
controls AND volume up/down) OR (image display).

.. code-block:: objc

   NSArray *videoCapabilities = @[
       kMediaPlayerPlayVideo,
       kMediaControlAny,
       kVolumeControlVolumeUpDown
   ];

   NSArray *imageCapabilities = @[
       kMediaPlayerDisplayImage
   ];

   CapabilityFilter *videoFilter =
       [CapabilityFilter filterWithCapabilities:videoCapabilities];
   CapabilityFilter *imageFilter =
       [CapabilityFilter filterWithCapabilities:imageCapabilities];

   [[DiscoveryManager sharedManager] setCapabilityFilters:@[videoFilter, imageFilter]];

Properties
----------

NSArray \* capabilities
   Array of capabilities required by this filter. This property is
   readonly use the addCapability or addCapabilities to build this
   object.

Methods
-------

\+ (:doc:`CapabilityFilter <ios-capabilityfilter>` \*) **filterWithCapabilities**:(NSArray \*)\ *capabilities*
   Create a CapabilityFilter with the given array required capabilities.

   **Parameters**

   * capabilities – Capabilities to be added to the new filter

\- (void) **addCapability**:(NSString \*)\ *capability*
   Add a required capability to the filter.

   **Parameters**

   * capability – Capability name to add (see capability header files for NSString constants)

\- (void) **addCapabilities**:(NSArray \*)\ *capabilities*
   Add array of required capabilities to the filter.

   **Parameters**

   * capabilities – List of capability names (see capability header files for NSString constants)
