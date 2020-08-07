DevicePickerDelegate
====================

The DevicePickerDelegate will receive a message when the user cancels or
selects a ConnectableDevice from the DevicePicker list. This is the
preferred method of selecting a device from DiscoveryManager.

Methods
-------

\- (void) **devicePicker**:(:doc:`DevicePicker <ios-devicepicker>` \*)\ *picker* **didSelectDevice**:(:doc:`ConnectableDevice <ios-connectabledevice>` \*)\ *device*
   When the user selects a ConnectableDevice from the DevicePicker's
   list, this method will be called with the selected ConnectableDevice.

   **Parameters:**

   * picker – DevicePicker that device was selected from
   * **didSelectDevice**: device – ConnectableDevice that was selected by the user

\- (void) **devicePicker**:(:doc:`DevicePicker <ios-devicepicker>` \*)\ *picker* **didCancelWithError**:(NSError \*)\ *error*
   This method is called if the user presses the cancel button in the
   picker or if Connect SDK forces a cancellation. If Connect SDK forces
   a cancellation, there will be an NSError object passed with the
   reason.

   **Parameters:**

   * picker – DevicePicker that was cancelled
   * **didCancelWithError**: error – NSError with a description of the failure
