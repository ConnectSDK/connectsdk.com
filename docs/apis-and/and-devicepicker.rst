DevicePicker
============
``com.connectsdk.device.DevicePicker``

Overview
--------

The DevicePicker is provided by the DiscoveryManager as a simple way for
you to present a list of available devices to your users.

In Depth
--------

By calling the getPickerDialog you will get a reference to the
AlertDialog that will be updated automatically updated as compatible
devices are discovered.

Methods
-------

**DevicePicker** (Activity *activity*)
    Creates a new DevicePicker

    **Parameters:**

    -  activity – Activity that DevicePicker will appear in

ListView **getListView** ()

void **pickDevice** (:doc:`ConnectableDevice <and-connectabledevice>` *device*)
    Sets a selected device.

    **Parameters:**

    -  device – Device that has been selected.

void **cancelPicker** ()
    Cancels pairing with the currently selected device.

AlertDialog **getPickerDialog** (String *message*, final OnItemClickListener *listener*)
    This method will return an AlertDialog that contains a ListView with
    an item for each discovered ConnectableDevice.

    **Parameters:**

    -  message – The title for the AlertDialog
    -  listener – The listener for the ListView to get the item that was clicked on
