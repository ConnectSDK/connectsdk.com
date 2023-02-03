Checking Capabilities
=====================

Setting up filters
------------------

When you are discovering devices you are able to specify multiple
capability filters.

.. code-block:: java

   CapabilityFilter videoFilter =
           new CapabilityFilter(
                   MediaPlayer.Display_Video,
                   MediaControl.Any,
                   VolumeControl.Volume_Up_Down);

   CapabilityFilter imageFilter =
           new CapabilityFilter(
                   MediaPlayer.Display_Image);

   DiscoveryManager.getInstance().setCapabilityFilters(videoFilter, imageFilter);

Any service that is found may meet the requirements of either filter but
not both. When getting the UI ready if a device might have a capability
you should always check before enabling that UI component.

.. code-block:: java

   myImageButton.setEnabled(mDevice.hasCapability(MediaPlayer.Display_Image));
