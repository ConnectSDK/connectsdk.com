Checking Capabilities
=====================

Setting up filters
------------------

When you are discovering devices you are able to specify multiple
capability filters.

.. code-block:: obj-c

   NSArray *videoCapabilities = @[
       kMediaPlayerDisplayVideo,
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

Any service that is found may meet the requirements of either filter but
not both. When getting the UI ready if a device might have a capability
you should always check before enabling that UI component.

.. code-block:: obj-c

   [myImageButton setEnabled:[self.device hasCapability:kMediaPlayerDisplayImage]];
