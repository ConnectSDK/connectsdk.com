CapabilityFilter
==========================================================
``com.connectsdk.discovery.CapabilityFilter``

CapabilityFilter is an object that wraps a List of required
capabilities. This CapabilityFilter is used for determining which
devices will appear in DiscoveryManager's compatibleDevices array.
The contents of a CapabilityFilter's array must be any of the string
constants defined in the Capability Class constants.

CapabilityFilter values
~~~~~~~~~~~~~~~~~~~~~~~

Here are some examples of values for the Capability constants.

* MediaPlayer.Display_Video = "MediaPlayer.Display.Video"
* MediaPlayer.Display_Image = "MediaPlayer.Display.Image"
* VolumeControl.Volume_Subscribe = "VolumeControl.Subscribe"
* MediaControl.Any = "MediaControl.Any"

All Capability header files also define a constant array of all
capabilities defined in that header (ex. kVolumeControlCapabilities).

AND/OR Filtering
~~~~~~~~~~~~~~~~

CapabilityFilter is an AND filter. A ConnectableDevice would need to
satisfy all conditions of a CapabilityFilter to pass.

The DiscoveryManager capabilityFilters is an OR filter. a
ConnectableDevice only needs to satisfy one condition
(CapabilityFilter) to pass.

Examples
~~~~~~~~

Filter for all devices that support video playback AND any media
controls AND volume up/down.

.. code-block:: java

  List<String> capabilities = new ArrayList<String>();
     capabilities.add(MediaPlayer.Display_Video);
     capabilities.add(MediaControl.Any);
     capabilities.add(VolumeControl.Volume_Up_Down);

  CapabilityFilter filter =
         new CapabilityFilter(capabilities);
  DiscoveryManager.getInstance().setCapabilityFilters(filter);

Filter for all devices that support (video playback AND any media
controls AND volume up/down) OR (image display).

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

Properties
----------

List<String> capabilities = new ArrayList<String>()
  .. container:: description

     List of capabilities required by this filter. This property is
     readonly use the addCapability or addCapabilities to build this
     object.

Methods
-------

**CapabilityFilter** ()
  .. container:: description

     Create an empty CapabilityFilter.

**CapabilityFilter** (String... *capabilities*)
  .. container:: description

     Create a CapabilityFilter with the given array of required
     capabilities.

  .. rubric:: Parameters:
     :name: parameters
     :class: method-detail-label

  .. container::

     -  capabilities –

        Capabilities to be added to the new filter

**CapabilityFilter** (List<String> *capabilities*)
  .. container:: description

     Create a CapabilityFilter with the given array of required
     capabilities.

  .. rubric:: Parameters:
     :name: parameters-4
     :class: method-detail-label

  .. container::

     -  capabilities –

        List of capability names (see capability class files for String
        constants)

void **addCapability** (String *capability*)
  .. container:: description

     Add a required capability to the filter.

  .. rubric:: Parameters:
     :name: parameters-1
     :class: method-detail-label

  .. container::

     -  capability –

        Capability name to add (see capability class files for String
        constants)

void **addCapabilities** (List<String> *capabilities*)
  .. container:: description

     Add array of required capabilities to the filter. (see capability
     class files for String constants)

  .. rubric:: Parameters:
     :name: parameters-2
     :class: method-detail-label

  .. container::

     -  capabilities –

        List of capability names

void **addCapabilities** (String... *capabilities*)
  .. container:: description

     Add array of required capabilities to the filter. (see capability
     classes files for String constants)

  .. rubric:: Parameters:
     :name: parameters-3
     :class: method-detail-label

  .. container::

     -  capabilities –

        String[] of capability names
