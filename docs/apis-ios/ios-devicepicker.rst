DevicePicker
============

Overview
--------

The DevicePicker is provided by the DiscoveryManager as a simple way for
you to present a list of available devices to your users.

In Depth
--------

The DevicePicker takes a sender parameter on the showPicker method. The
sender parameter is used to display a popover from a particular UIView
on iPads.

You should not attempt to instantiate the DevicePicker on your own.
Instead, get the reference from the DeviceManager with [[DeviceManager
sharedManager] devicePicker];

Properties
----------

id<:doc:`DevicePickerDelegate <ios-devicepickerdelegate>`> delegate
   Delegate that receives selected/cancelled messages.

BOOL shouldAnimatePicker
   When the showPicker method is called, it can animate onto the screen
   if this value is set to YES. This value will also be used to
   determine if the picker should animate when it is dismissed.

BOOL shouldAutoRotate
   When the device is rotated, the DevicePicker can automatically adjust
   the view to compenstate. Default is NO.

:doc:`ConnectableDevice <ios-connectabledevice>` \* currentDevice
   If you wish to show a checkmark next to a device in the picker, you
   can set that device object to currentDevice. The setter for
   currentDevice will also reload the tableView in the picker.

Methods
-------

\- (void) **showPicker**:(id)\ *sender*
   This method will animate the picker onto the screen. On iPad, the
   picker will appear as a popover view and will animate from the sender
   object, if you provide one. On iPhone, the picker will appear as a
   full-screen table view that will animate up from the bottom of the
   screen. This picker will animate in real time with additions, losses,
   and updates of ConnectableDevices.

   **Parameters:**

   *  sender – On iPad, this should be a UIView for the popover view to animate from. On iPhone, this property is ignored.

\- (void) **showActionSheet**:(id)\ *sender*
   This method will animate an action sheet onto the screen containing a
   button for each discovered ConnectableDevice. Due to the nature of
   action sheets, it is not possible to update the action sheet after it
   has appeared. It is recommended to use the showPicker: method if you
   want a picker that will update in real time.

   **Parameters:**

   *  sender – The UIView that the action sheet should appear in
